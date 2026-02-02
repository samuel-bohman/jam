#!/usr/bin/env bash

# http://mw-fceedfe8-predictor.amd-internal.svc.cluster.local/v1/chat/completions
BASE_URL="http://mw-fceedfe8-predictor.amd-internal.svc.cluster.local"
ENDPOINT="/v1/chat/completions"
MODEL="openai/gpt-oss-20b"

vllm bench serve \
  --backend openai-chat \
  --base-url "${BASE_URL}" \
  --endpoint "${ENDPOINT}" \
  --model "${MODEL}" \
  --dataset-name random \
  --random-input-len 2048 \
  --random-output-len 128 \
  --num-prompts 500 \
  --max-concurrency 1 \
  --ready-check-timeout-sec 60 \
  --trust-remote-code
