.. _compatibility_matrix:

Compatibility Matrix
====================

The table below shows mutually exclusive features along with support for some device types. 

.. list-table::
   :header-rows: 1
   :widths: 20 8 8 8 8 8 8 8 8 8 8 8

   * - Feature
     - Chunked Prefill
     - APC
     - LoRa
     - Prompt Adapter
     - Speculative decoding
     - CUDA Graphs
     - Encoder/Decoder
     - Logprobs
     - Prompt Logprobs
     - Async Output
     - Multi-step
   * - APC
     - ✅
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
   * - LoRa
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/config.py#L1558>`__ 
     - ✅
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
   * - Prompt Adapter
     - ✅
     - ✅
     - ✅
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
   * - Speculative decoding
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/config.py#L1200>`__  `[T] <https://github.com/vllm-project/vllm/issues/5016>`__ 
     - ✅
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/spec_decode/spec_decode_worker.py#L86-L87>`__ 
     - ✅
     - 
     - 
     - 
     - 
     - 
     - 
     - 
   * - CUDA Graphs
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - 
     - 
     - 
     - 
     - 
     - 
   * - Encoder/Decoder
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/worker/utils.py#L25>`__ 
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/worker/utils.py#L17>`__ `[T] <https://github.com/vllm-project/vllm/issues/7366>`__ 
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/worker/utils.py#L35>`__ 
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/worker/utils.py#L55>`__ 
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/worker/utils.py#L47>`__ `[T] <https://github.com/vllm-project/vllm/issues/7366>`__ 
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/worker/utils.py#L51>`__ `[T] <https://github.com/vllm-project/vllm/issues/7447>`__ 
     - 
     - 
     - 
     - 
     - 
   * - Logprobs
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - 
     - 
     - 
     - 
   * - Prompt Logprobs
     - ✅
     - ✅
     - ✅
     - ✅
     - ✗ `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/engine/output_processor/multi_step.py#L65>`__  `[T] <https://github.com/vllm-project/vllm/pull/8199>`__ 
     - ✅
     - ✅
     - ✅
     - 
     - 
     - 
   * - Async Output
     - ✅
     - ✅
     - ✅
     - ✅
     - ✗ `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/config.py#L396>`__ 
     - ✅ `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/config.py#L383>`__ 
     - ✗ `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/config.py#L200>`__  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/worker/utils.py#L51>`__ 
     - ✅
     - ✅
     - 
     - 
   * - Multi-step
     - ✗ `[C] <https://github.com/vllm-project/vllm/blob/7de49aa86c7f169eb0962b6db29ad53fff519ffb/vllm/engine/arg_utils.py#L944>`__ 
     - ✅
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/engine/output_processor/multi_step.py#L130>`__ 
     - ✅
     - ✗ `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/engine/arg_utils.py#L951>`__ 
     - ✅
     - ✗ `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/worker/utils.py#L47>`__ 
     - ✅
     - ✗ `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/engine/output_processor/multi_step.py#L65>`__ `[T] <https://github.com/vllm-project/vllm/issues/8198>`__ 
     - ✅
     - 
   * - NVIDIA
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
   * - CPU
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/engine/arg_utils.py#L954>`__ 
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/executor/cpu_executor.py#L345>`__ 
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/executor/cpu_executor.py#L31>`__ `[T] <https://github.com/vllm-project/vllm/pull/4830>`__ 
     - ✗ `[T] <https://github.com/vllm-project/vllm/issues/8475>`__ 
     - ✅
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/executor/cpu_executor.py#L327>`__ 
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a84e598e2125960d3b4f716b78863f24ac562947/vllm/worker/cpu_model_runner.py#L125>`__ 
     - ✅
     - ✅
     - ✗ `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/config.py#L370>`__ 
     - ✗ `[T] <https://github.com/vllm-project/vllm/issues/8477>`__ 
   * - AMD
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✗  `[C] <https://github.com/vllm-project/vllm/blob/a2469127db6144eedb38d0b505287c0044e4ce06/vllm/attention/backends/rocm_flash_attn.py#L343>`__ 
     - ✅
     - ✅
     - ✅
     - ✗ `[T] <https://github.com/vllm-project/vllm/issues/8472>`__ 
     
Note:

- [C] stands for code checks, that is, there is a checking on running that verify if the combinations is valid and raises and error or log a warning disabling the feature. 
- [T] stands for tracking issues or pull requests on vLLM Repo.
- APC stands for Automatic Prefix Caching.
- Async output processing needs CUDA Graphs activated to work, there is a code check in the table to inform that. It is the only ✅ with a [C].
- Encoder/decoder currently does not work with CUDA Graphs, therefore it is not compatible with Async output processing as well. 


..
  TODO: Add support for remaining devices.