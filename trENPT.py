from transformers import MarianMTModel, MarianTokenizer
import streamlit as st
import warnings


@st.cache_resource
def translate_text(text):
    model_name = 'Helsinki-NLP/opus-mt-tc-big-en-pt'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    input_ids = tokenizer.encode(text, add_special_tokens=True, return_tensors="pt")
    translated = model.generate(input_ids)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text


warnings.filterwarnings("ignore")
st.write("""# Inglês para Português""")
prompt = st.text_input("Texto em Inglês: ")
if st.button('Send'): 
    response = translate_text(prompt)
    st.write("""Portugês: """, response)
