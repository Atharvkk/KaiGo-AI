from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import torch

if torch.cuda.is_available():
    device = torch.device("cuda")
    print("GPU is available and being used.")
else:
    device = torch.device("cpu")
    print("GPU is not available, using CPU instead.")
model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
human_prompt = "I'm scared of the dark!"
gptprompt = f"What is something a caretaker comforting a neurodivergent individual would say in response to '{human_prompt}'?"

inputs = tokenizer(gptprompt, return_tensors="pt").to(device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_length=150,
        num_return_sequences=1,
        temperature=0.4,
        top_k=50,
        top_p=0.95,
        do_sample=True
    )
realop = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(realop)