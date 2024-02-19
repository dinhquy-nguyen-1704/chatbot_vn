import transformers
from config import get_config
from huggingface_hub import notebook_login

def train(model, tokenizer, data):

    config = get_config()

    training_args = transformers.TrainingArguments(
        output_dir=config.output_dir,
        per_device_train_batch_size=config.per_device_train_batch_size,
        gradient_accumulation_steps=4,
        num_train_epochs=config.num_train_epochs,
        learning_rate=config.learning_rate,
        fp16=True,
        save_total_limit=3,
        logging_steps=1,
        optim="paged_adamw_8bit",
        lr_scheduler_type="cosine",
        warmup_ratio=0.05,
        push_to_hub=config.push_to_hub,
    )
    trainer = transformers.Trainer(
        model=model,
        train_dataset=data,
        args=training_args,
        data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False)
    )
    model.config.use_cache = False

    return trainer, model