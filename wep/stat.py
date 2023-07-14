import os
import openai
from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# import opinai_key

load_dotenv(find_dotenv())
openai.api_key=os.environ['OPEN_AI_KEY'] 

#cretivty
llm = OpenAI(temperature=0.6)
llm = OpenAI(model_name="text-ada-001")
#promt template ,chain
prompt_template_Q1= PromptTemplate (
    input_variables= ["something"],
    template= "what" 
)
prompt_template_Q1.format(something = "tax")

chain = LLMChain(llm=llm , prompt=prompt_template_Q1)
