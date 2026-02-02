# AI Acceleration with AMD (ROCm/Enterprise AI Suite)

Welcome to the official repository for the AI Acceleration with AMD hands-on lab at HPE Tech Jam Vienna 2026! This repository is dedicated to sharing files, resources, and materials relevant to the hands-on lab.

## Repository Contents

### Fine-Tuning Dataset

- **fine_tuning_dataset.jsonl**
A JSONL file containing sample data for fine-tuning language models. Each line represents a training example with a prompt and corresponding completion.

### vLLM Benchmarking Scripts

- **vllm_bench_setup.sh**
Bash script to set up a Python virtual environment and install the vLLM library for benchmarking. Run this before using the benchmark script.

- **vllm_bench.sh**
Bash script to run a benchmark using the vLLM library against a chat completions API endpoint.

### Streaming Response

- **streamed_response.py**
Example Python script demonstrating how to interact with a chat completions API using streamed responses. This approach allows the response to appear incrementally—simulating a real-time typing effect—rather than displaying the entire output at once.

### ComfyUI Text-to-Image Generation

- **comfyui_sample.json**
A sample ComfyUI workflow (canvas file) for generating images using Flux AI model. Drag and drop this file into ComfyUI to load the workflow.

## Workshop publication note

These materials were prepared and will be used in a hands-on lab run at the HPE Tech Jam Vienna 2026 event. The repository is published publicly to allow participants free access during the workshop. If you find any content that appears to contain secrets, PII, or other sensitive information, notify the maintainer immediately.

## Disclaimer

This repository contains sample scripts and datasets intended for workshop/demo purposes only. Some example scripts in this repo use insecure defaults (e.g., disabling TLS verification); do not use those defaults in production. Review any dataset files for PII or copyright restrictions before using them.

## License

This project is licensed under the MIT License — see the included LICENSE file for full terms.