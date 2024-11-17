# pip install --upgrade langchain langhchain-google-genai streamlit
# from langchain import LLMchain

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import os


os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# create prompt template for generating taglines

tagline_template = "Give me {number} funny taglines about {topic}"

tagline_prompt = PromptTemplate(template = tagline_template, input_variables = ['number','topic'])

#Initialize Google's Gemeni model

gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

#Create LLM chain using the prompt template and model
tagline_chain = tagline_prompt | gemini_model

#Example of using the LLM chain
# response = tagline_chain.invoke({"number": 5, "topic": "population of India"})



import streamlit as st

st.header("Funny taglines Generator")

st.subheader("Generate taglines using Gen AI")

topic = st.text_input("Topic")

number = st.number_input("Number of taglines", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Generate"):
    taglines = tagline_chain.invoke({"number": number, "topic": topic})
    st.write(taglines.content)

