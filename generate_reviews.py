from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

def generate_review(prompt):
    model_name = "tiiuae/falcon-7b"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Adjust torch_dtype to float32 for better compatibility with M1 Mac
    text_generator = pipeline(
        "text-generation",
        model=model_name,
        tokenizer=tokenizer,
        torch_dtype=torch.float32,
        trust_remote_code=True,
        device_map="auto"
    )
    
    sequences = text_generator(prompt, max_length=200, do_sample=True, top_k=10, num_return_sequences=1)
    return sequences[0]["generated_text"]
