import torch
from transformers import pipeline

# Specify the model you have access to, e.g., Llama-3-8B-Instruct
model_id = "meta-llama/Llama-3.1-8B-Instruct"

# Create a text-generation pipeline
# device_map="auto" efficiently uses available resources (like GPU if present)
# torch.float16 is used for optimized performance and memory usage
pipeline = pipeline(
    task="text-generation",
    model=model_id,
    device_map="auto",
    torch_dtype=torch.float16,
)

# Define your "hello world" prompt
prompt = "Hello world! This is a simple test to see if the Llama model is working."

# Generate text based on the prompt
outputs = pipeline(prompt, max_new_tokens=50)

# Print the generated text
print(outputs[0]['generated_text'])

