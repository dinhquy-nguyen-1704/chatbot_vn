# chatbot_vn
## Introduction
This repository is designed to help you get started with building and fine-tuning your own AI chatbot in Vietnamese. The default model used in this repository is [vinallama-7b-chat](https://huggingface.co/vilm/vinallama-7b-chat) and the default dataset is [chatbot_instruction_prompts](https://huggingface.co/datasets/alespalla/chatbot_instruction_prompts).
<p align="center">
  <img width="800" alt="sample data" src="https://github.com/dinhquy-nguyen-1704/chatbot_vn/assets/127675330/10baed6e-2d9e-440f-8f94-646ac31773cc">
</p>
<p align="center">
  <em>Some sample data from the dataset</em>
</p>

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

## Training
To train the model, run the following command:
```
python main.py
```
> You can also adjust the following parameters for the training process: 
```
--model: name of the trained model file
--dataset: dataset used for fine-tuning
--output_dir: name of the model on HuggingFace after training
--max_new_tokens: maximum number of new tokens that can be generated in the output
--temperature: controls the randomness of the output’s predictions
--top_p: known as nucleus sampling, this parameter decides the number of words to consider for each prediction
--num_return_sequences: specifies the number of sequences to generate
```

## Inference
To use the trained model, run the following command:
```
python infer.py --model_hf_name model_name --text your_text
```
> Where:
```
model_name: name of the trained model on HuggingFace
your_text: your question for model
```

## Contact
If you have any questions or feedback, please open an issue in this repository.

## References
- AIO2023
- [HuggingFace](https://huggingface.co/)
- [VinaLLaMA](https://www.vilm.org/research/introducing-vinallama)

Happy coding!
