import os
import openai
import streamlit as st
from theKey import opinai_key
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# import opinai_key

os.environ["OPENAI_API_KEY"] = opinai_key

#cretivty
llm = OpenAI(temperature=0.9)

#chat 
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = ChatOpenAI(temperature=0.9)
chat.predict_messages([HumanMessage(content=".")])

#Prompt templates
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")
#Agent
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

# First,  load the language model we're going to use to control the agent.
chat = ChatOpenAI(temperature=0)

# Next, load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Finally,  initialize an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(tools, chat, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Now  test it out!
agent.run("Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?")
# memory 
from langchain import OpenAI, ConversationChain

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

conversation.run("Hi there!")

# Streamlit app configuration
import streamlit as st
st.set_page_config(page_title="جباية", layout="wide")

# Writing the app main function
def main():

 # Setting up the app title and description
    st.title("BatataBot: Your Friendly Tour Guide")

st.write("Ask any question,  provide answers!")

# Available e types for the checklist
grope_types = ['اشتراك ', 'تسجيل دخول', 'اكمل كضيف']
# User selection for the type of places to visit
selected_types = st.multiselect("Select the type of places you want to visit", grope_types)
if __name__ == "__main__":
    main()
