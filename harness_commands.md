# Harness Commands (Draft)

## Base model

lm-eval --model hf
--model_args pretrained=meta-llama/Llama-3-8B-Instruct
--tasks gsm8k --device cuda:0 --batch_size 2

## With LoRA (PEFT)

lm-eval --model hf
--model_args pretrained=meta-llama/Llama-3-8B-Instruct,peft=outputs/lora-llama3-8b/peft
--tasks boolq --device cuda:0 --batch_size 2
