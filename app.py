from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## FUNCTION TO LOAD GEMINI PRO MODEL & GET RESPONSE

model=genai.GenerativeModel("gemini-2.5-flash")
def get_gemini_response(question):
    result=model.generate_content(question)
    return result.text

st.set_page_config(
    page_title="Q&A DEMO",
    page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-7t5AkQU2WfIb4fC2lyOtPrko_Ku9lQkxnw&s"
)

st.title("💬 Gemini Q&A Demo")

input=st.text_input("Input",key="Input")
submit=st.button("Ask the question")
#when submit is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The response is:")
    st.write(response)

