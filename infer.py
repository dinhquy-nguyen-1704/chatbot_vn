import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from config import get_config

def main():

    config = get_config()

    model_hf_name = config.model_hf_name

    model = AutoModelForCausalLM.from_pretrained(model_hf_name)
    tokenizer = AutoTokenizer.from_pretrained(model_hf_name)

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    generation_config = model.config

    prompt = f"""
    <|im_start|>system
    Bạn là một trợ lý AI hữu ích. Hãy trả lời người dùng một cách chính xác.
    <|im_end|>
    <|im_start|>user
    {config.text}
    <|im_end|>
    <|im_start|>assistant
    """.strip()

    encoding = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.inference_mode():
        outputs = model.generate(
            input_ids=encoding.input_ids,
            attention_mask=encoding.attention_mask,
            **generation_config
        )
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))

if __name__ == '__main__':
    main()