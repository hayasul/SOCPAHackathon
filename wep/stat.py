import os
#from theKey import opinai_key
from langchain.llms import OpenAI

#the key
os.environ['OPEN_AI_KEY'] = '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'
#cretivty
llm = OpenAI(temperature=0.6)

#promt template
from langchain.prompts import PromptTemplate

prompt_template_Q1= PromptTemplate (
    input_variables= ["something"],
    template= "what" 
)
prompt_template_Q1.format(something = "tax")

#
from langchain.chains import LLMChain

chain = LLMChain(llm=llm , prompt=prompt_template_Q1)
