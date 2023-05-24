from transformers import MarianMTModel, MarianTokenizer
import streamlit as st

model_name = 'Helsinki-NLP/opus-mt-tc-big-en-pt'
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

def translate_text(text):
    input_ids = tokenizer.encode(text, add_special_tokens=True, return_tensors="pt")
    translated = model.generate(input_ids)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

st.write("""# Inglês para Português""")
st.write("""Tradução de EN para PT""")
prompt = st.text_input("Texto em Inglês: ")
if st.button('Send'): 
    response = translate_text(prompt)
    st.write("""Portugês: """, response)
