from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model= genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_res(input,image):
    if input !="":

        response=model.generate_content(input,image)
    else:
        response=model.generate_content(image)
        return response.text

st.set_page_config(page_title="Gemini image Demo")

st.header("Gemini Application")

input =st.text_input("input Prompt: ",key="input")

upload_image = st.file_uploader("Choose the image ...",type=["jpg","jpeg","png"])
image=""
if upload_image is not None:
    image=Image.open(upload_image)
    st.image(image,caption="upload image",use_column_width=True)

submit =st.button("tell me about image")

if submit:
    response = get_gemini_res(input,image)
    st.subheader("the response is")
    st.write(response)