import os
import openai
#from dotenv import load_dotenv, find_dotenv
from theKey import opinai_key
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# import opinai_key
#تصلح الكي:)
os.environ["OPENAI_API_KEY"] = opinai_key

#cretivty
llm = OpenAI(temperature=0.6)
llm = OpenAI(model_name="text-ada-001")

#promt template ,chain(بارت كيف نعلم النموذج بتعليماتنا)

prompt_template_Q1= PromptTemplate (
    input_variables= ["something"],
    template= "what" 
)
prompt_template_Q1.format(something = "tax")

chain = LLMChain(llm=llm , prompt=prompt_template_Q1)
# memory ?

# Streamlit app configuration
import streamlit as st
st.set_page_config(page_title="جباية", layout="wide")

 # Setting up the app title and description
st.title("اكتب")
st.write("Ask any question,  provide answers!")

    # Available e types for the checklist
place_types = ['Shopping', 'Food', 'Activities']