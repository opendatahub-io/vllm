"""Compare the outputs of HF and vLLM for Mistral models using greedy sampling.

Run `pytest tests/models/embedding/language/test_embedding.py`.
"""
import os

import pytest
import torch
import torch.nn.functional as F

MODELS = [
    "BAAI/bge-base-en-v1.5",
    "intfloat/e5-mistral-7b-instruct",
    "BAAI/bge-multilingual-gemma2",
]

ENCODER_MODELS = ["BAAI/bge-base-en-v1.5"]


def compare_embeddings(embeddings1, embeddings2):
    similarities = [
        F.cosine_similarity(torch.tensor(e1), torch.tensor(e2), dim=0)
        for e1, e2 in zip(embeddings1, embeddings2)
    ]
    return similarities


@pytest.mark.parametrize("model", MODELS)
@pytest.mark.parametrize("dtype", ["half"])
def test_models(
    hf_runner,
    vllm_runner,
    example_prompts,
    model: str,
    dtype: str,
) -> None:

    prior_attn_backend_env = os.getenv("VLLM_ATTENTION_BACKEND", None)
    if model in ENCODER_MODELS:
        os.environ["VLLM_ATTENTION_BACKEND"] = "XFORMERS"

    # The example_prompts has ending "\n", for example:
    # "Write a short story about a robot that dreams for the first time.\n"
    # sentence_transformers will strip the input texts, see:
    # https://github.com/UKPLab/sentence-transformers/blob/v3.1.1/sentence_transformers/models/Transformer.py#L159
    # This makes the input_ids different between hf_model and vllm_model.
    # So we need to strip the input texts to avoid test failing.
    example_prompts = [str(s).strip() for s in example_prompts]

    with hf_runner(model, dtype=dtype, is_embedding_model=True) as hf_model:
        hf_outputs = hf_model.encode(example_prompts)

    with vllm_runner(model, dtype=dtype, max_model_len=None) as vllm_model:
        vllm_outputs = vllm_model.encode(example_prompts)

    similarities = compare_embeddings(hf_outputs, vllm_outputs)
    all_similarities = torch.stack(similarities)
    tolerance = 1e-2
    assert torch.all((all_similarities <= 1.0 + tolerance)
                     & (all_similarities >= 1.0 - tolerance)
                     ), f"Not all values are within {tolerance} of 1.0"

    if "VLLM_ATTENTION_BACKEND" in os.environ:
        if prior_attn_backend_env is None:
            del os.environ["VLLM_ATTENTION_BACKEND"]
        else:
            os.environ["VLLM_ATTENTION_BACKEND"] = prior_attn_backend_env
