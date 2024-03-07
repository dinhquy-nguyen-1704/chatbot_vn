# chatbot_vn
## Introduction
This repository is designed to help you get started with building and fine-tuning your own AI chatbot in Vietnamese. The default model used in this repository is [vinallama-7b-chat](https://huggingface.co/vilm/vinallama-7b-chat) and the default dataset is [chatbot_instruction_prompts]([url](https://huggingface.co/datasets/alespalla/chatbot_instruction_prompts)).

## Getting Started
```
git clone https://github.com/dinhquy-nguyen-1704/chatbot_vn.git
```
```
cd /kaggle/working/chatbot_vn
```
```
pip install -r requirements.txt
```
Log in to Hugging Face and create a New Token with **write** mode.
```
python -c "from huggingface_hub.hf_api import HfFolder; HfFolder.save_token('your_token')"
```
## Contact
If you have any questions or feedback, please open an issue in this repository.

Happy coding!
