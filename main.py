import warnings
warnings.simplefilter("ignore")

from config import get_config
from utils import *
from train import train

import torch
import torch.nn as nn

from datasets import load_dataset

def main():

    config = get_config()

    model_name = config.model
    model, tokenizer = model_tokenizer(model_name)

    generation_config = model.generation_config
    generation_config.max_new_tokens = config.max_new_tokens
    generation_config.temperature = config.temperature
    generation_config.top_p = config.top_p
    generation_config.num_return_sequences = config.num_return_sequences
    generation_config.pad_token_id = tokenizer.eos_token_id
    generation_config.eos_token_id = tokenizer.eos_token_id
    dataset = config.dataset

    data = load_dataset(dataset)
    data = data['train'].shard(num_shards=50, index=0).filter(lambda sample: sample['response'] != '' and sample['prompt'] != '').shuffle().map(lambda sample: generate_and_tokenize_prompt(sample, tokenizer))

    trainer, model = train(model, tokenizer, data)
    trainer.train()
    trainer.push_to_hub(commit_message="Training complete")

if __name__ == '__main__':
    main()