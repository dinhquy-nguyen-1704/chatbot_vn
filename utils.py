import warnings
warnings.simplefilter("ignore")

import torch
from googletrans import Translator

from peft import (
    LoraConfig,
    get_peft_model,
    prepare_model_for_kbit_training
)

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig 
)

def model_tokenizer(model_name):

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        trust_remote_code=True,
        quantization_config=bnb_config
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token

    model.gradient_checkpointing_enable()
    model = prepare_model_for_kbit_training(model)

    config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=[
            "q_proj",
            "up_proj",
            "o_proj",
            "k_proj",
            "down_proj",
            "gate_proj",
            "v_proj"
        ],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )
    model = get_peft_model(model, config)

    return model, tokenizer

def generate_prompt(data_point):
    translator = Translator()
    vn_prompt = translator.translate(data_point['prompt'], src='en', dest='vi').text
    vn_response = translator.translate(data_point['response'], src='en', dest='vi').text

    return f"""
<|im_start|>system
Bạn là một trợ lý AI hữu ích. Hãy trả lời người dùng một cách chính xác.
<|im_end|>
<|im_start|>user
{vn_prompt}
<|im_end|>
<|im_start|>assistant
{vn_response}
""".strip()

def generate_and_tokenize_prompt(data_point, tokenizer):
    full_prompt = generate_prompt(data_point)
    tokenized_full_prompt = tokenizer(full_prompt, padding=True, truncation=True)
    return tokenized_full_prompt