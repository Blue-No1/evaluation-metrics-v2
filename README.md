# Evaluation Metrics

Semi-hands-on evaluation notes + commands (perplexity, exact-match, task probes).
Ghi chú & lệnh chạy đánh giá.

## Plan
- `lm-eval-harness` basic runs.
- Tiny custom probes (math/code snippets).
- Compare base vs LoRA checkpoints (later).

## Quick Start (conceptual)
```bash
pip install lm-eval
lm-eval --model hf \
  --model_args pretrained=meta-llama/Llama-3-8B-Instruct \
  --tasks hellaswag,boolq \
  --device cuda:0 --batch_size 4
