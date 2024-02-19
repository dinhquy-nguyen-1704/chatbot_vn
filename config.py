import argparse

def get_config():
    parser = argparse.ArgumentParser()

    parser.add_argument('--model', type=str, default='vilm/vinallama-7b-chat')
    parser.add_argument('--max_new_tokens', type=int, default=200)
    parser.add_argument('--temperature', type=float, default=0.7)
    parser.add_argument('--top_p', type=float, default=0.7)
    parser.add_argument('--num_return_sequences', type=int, default=1)
    parser.add_argument('--dataset', type=str, default='alespalla/chatbot_instruction_prompts')
    parser.add_argument('--output_dir', type=str, default='vinallama-7b-chat-finetune-chatbot_instruction_prompts')
    parser.add_argument('--per_device_train_batch_size', type=int, default=4) 
    parser.add_argument('--num_train_epochs', type=int, default=1) 
    parser.add_argument('--learning_rate', type=float, default=2e-4)
    parser.add_argument('--push_to_hub', type=bool, default=True)
    parser.add_argument('--model_hf_name', type=str, default=None)  
    parser.add_argument('--text', type=str, default=None)  

    args = parser.parse_args()

    return args