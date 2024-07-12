import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
model.eval() 

def create_caption(description):
    input_text = "Write a hilariously witty instagram caption in one sentence for a photo that shows "+description
    #input_ids = tokenizer.encode(input_text, return_tensors='pt')
    inputs = tokenizer(input_text, return_tensors='pt')
    with torch.no_grad():
        outputs = model.generate(input_ids=inputs['input_ids'],
        attention_mask=inputs['attention_mask'],
        max_length=100,
        temperature=0.7,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        early_stopping=False)
        
    for output in outputs:
        generated_text = tokenizer.decode(output, skip_special_tokens=True)
    
    print("gen : "+generated_text[len(input_text)+2:])
    print(len(generated_text))
    return generated_text[len(input_text)+2:]

