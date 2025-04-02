# SPDX-License-Identifier: Apache-2.0
import copy
import json
from re import escape as regex_escape

import llguidance
from transformers import PreTrainedTokenizerBase

from vllm.model_executor.guided_decoding.guidance_logits_processors import (
    GuidanceLogitsProcessor)
from vllm.sampling_params import GuidedDecodingParams


def _walk_json_for_additional_properties(data: object):
    if isinstance(data, dict):
        for value in data.values():
            _walk_json_for_additional_properties(value)
        if 'additionalProperties' not in data and \
            ('properties' in data or 'patternProperties' in data):
            data['additionalProperties'] = False
    elif isinstance(data, list):
        for item in data:
            _walk_json_for_additional_properties(item)


def get_local_guidance_guided_decoding_logits_processor(
        guided_params: GuidedDecodingParams,
        tokenizer: PreTrainedTokenizerBase) -> GuidanceLogitsProcessor:
    """
    Given an OpenAI-compatible request, check for guided decoding parameters
    and get the necessary logits processor for the given guide.
    """

    grm = ""
    if (guide_json := guided_params.json) is not None:
        # Optionally set additionalProperties to False at the top-level
        # By default, other backends do not allow additional top-level
        # properties, so this makes guidance more similar to other backends
        if 'no-additional-properties' in guided_params.backend_options():
            if isinstance(guide_json, str):
                guide_json = json.loads(guide_json)
            else:
                # copy for modifications
                guide_json = copy.deepcopy(guide_json)
            _walk_json_for_additional_properties(guide_json)

        grm = llguidance.LLMatcher.grammar_from_json_schema(
            guide_json,
            overrides={"whitespace_pattern": guided_params.whitespace_pattern})
    elif guided_params.json_object:
        grm = llguidance.LLMatcher.grammar_from_json_schema(
            '{"type": "object"}',
            overrides={"whitespace_pattern": guided_params.whitespace_pattern})
    elif guided_params.regex:
        grm = llguidance.grammar_from("regex", guided_params.regex)
    elif guided_params.choice:
        # choice just uses regex
        choices = (regex_escape(str(choice))
                   for choice in guided_params.choice)
        choices_regex = "(" + "|".join(choices) + ")"
        grm = llguidance.grammar_from("regex", choices_regex)
    elif guided_params.grammar:
        # this supports Lark and GBNF
        grm = llguidance.grammar_from("grammar", guided_params.grammar)

    if grm:
        return GuidanceLogitsProcessor(grm, tokenizer)

    raise ValueError("Unknown guided decoding mode")
