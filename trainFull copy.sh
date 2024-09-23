#!/bin/bash
REQUIRED_GPUS=4  # The number of GPUs you wish to use
batch_size=16
accumula=$((64/$REQUIRED_GPUS/$batch_size))

datasets=('yourDataset')   # change To your dataset

model="yourPath/Llama-2-7b-chat-hf"
model_name=${model##*/}
declare -A modelTOTemplate=(["llama-7b-hf"]="alpaca" ["llama-13b-hf"]="alpaca" ["Llama-2-7b-hf"]="alpaca" ["llama-2-13b-hf"]="alpaca" ["Llama-2-13b-chat-hf"]="llama2" ["Llama-2-7b-chat-hf"]="llama2" ["bloomz-7b1-mt"]="alpaca" ["bayling-13b-v1.1"]="Bayling" ["chinese-llama-7b"]="alpaca" ["chinese-llama-13b"]="alpaca" ["hfl_chinese-llama-2-7b"]="alpaca" ["hfl_chinese-llama-2-13b"]="alpaca" ["chinese_llama2_7b"]="alpaca" ["m-llama"]="alpaca" ['bloom-7b1']="alpaca" ['Baichuan2-13B-Chat']="baichuan2")
echo "model_name: $model_name"
template=${modelTOTemplate[$model_name]}
declare -A lora_targetS=(["llama-7b-hf"]="q_proj,v_proj" ["llama-13b-hf"]="q_proj,v_proj" ["Llama-2-7b-hf"]="q_proj,v_proj" ["llama-2-13b-hf"]="q_proj,v_proj" ["Llama-2-13b-chat-hf"]="q_proj,v_proj" ["Llama-2-7b-chat-hf"]="q_proj,v_proj" ["bloomz-7b1-mt"]="query_key_value" ["bayling-13b-v1.1"]="q_proj,v_proj" ["chinese-llama-7b"]="q_proj,v_proj" ["chinese-llama-13b"]="q_proj,v_proj" ["hfl_chinese-llama-2-7b"]="q_proj,v_proj" ["hfl_chinese-llama-2-13b"]="q_proj,v_proj" ["chinese_llama2_7b"]="q_proj,v_proj" ["m-llama"]="q_proj,v_proj" ['bloom-7b1']="query_key_value" ['Baichuan2-13B-Chat']="W_pack")
lora_target=${lora_targetS[$model_name]}
echo "lora_target: $lora_target"


MASTER_PORT=$(python -c 'import socket; s = socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')

FREE_GPUS=$(python -c "
import subprocess
import re
import sys

def find_free_gpus():
    output = subprocess.check_output(['nvidia-smi', '--query-gpu=utilization.gpu,memory.free', '--format=csv,nounits,noheader'], universal_newlines=True)
    lines = output.strip().split('\\n')
    free_gpus = []
    for i, line in enumerate(lines):
        util, mem = map(int, re.split(',\\s*', line))
        if mem > 10000:
            free_gpus.append(str(i))

    if len(free_gpus) < $REQUIRED_GPUS:
        sys.stderr.write(f'Error: Not enough free GPUs. Required: $REQUIRED_GPUS, Available: {len(free_gpus)}\\n')
        sys.exit(1)

    print(','.join(free_gpus[:$REQUIRED_GPUS]))

find_free_gpus()
")
echo "Using GPUs: $FREE_GPUS"
if [ $? -ne 0 ]; then
    exit 1
fi
learning_rateS=(2e-5 4e-5 8e-5)
steps=(300)
for step in "${steps[@]}"; do
    for lr in "${learning_rateS[@]}"; do
        for dataset in "${datasets[@]}"; do
            echo "dataset: $dataset"
            output_dir="./full2/$model_name/$dataset$lr"_"$step"
            deepspeed --include localhost:$FREE_GPUS --master_port=$MASTER_PORT yourPath/LLaMA-Efficient-Tuning/src/train_bash.py \
                --deepspeed yourPath/LLaMA-Efficient-Tuning/ds_config.json \
                --stage sft \
                --model_name_or_path $model \
                --do_train \
                --dataset  $dataset \
                --template $template \
                --finetuning_type  full \
                --output_dir  $output_dir \
                --overwrite_cache \
                --per_device_train_batch_size $batch_size \
                --gradient_accumulation_steps  $accumula \
                --lr_scheduler_type cosine \
                --logging_steps 10 \
                --learning_rate $lr \
                --max_steps $step \
                --plot_loss \
                --fp16 \
                --save_strategy steps \
                --save_steps 400 \

                
            echo "del $output_dir目录下的每个checkpoint文件夹内的global_step文件夹"
            find "yourPath/LLaMA-Efficient-Tuning/${output_dir#./}" -path '*/checkpoint-*/global_step*' -type d -exec rm -rf {} +
        done
    done
done
