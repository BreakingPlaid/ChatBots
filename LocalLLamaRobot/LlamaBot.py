import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
model_name = "distilgpt2"  # Replace with your chosen model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Streamlit app setup
st.set_page_config(page_title="LLM Demo", layout="centered")
st.title("Local LLM Demonstration")

# Get user input
prompt = st.text_area("Enter your prompt:", "")
max_new_tokens = st.slider("Max New Tokens", 10, 200, 50)
generate = st.button("Generate")

# Generate response on button click
if generate and prompt:
    with torch.no_grad():
        inputs = tokenizer(prompt, return_tensors="pt", padding=True)
        outputs = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_new_tokens=max_new_tokens,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    st.write("Response:", response)