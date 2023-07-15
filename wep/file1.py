import os
import sys
import openai
import streamlit as st
from theKey import opinai_key
from langchain.document_loaders import GCSFileLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# import opinai_key

os.environ["OPENAI_API_KEY"] = opinai_key

#chat 

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = ChatOpenAI(temperature=0.9)
chat.predict_messages([HumanMessage(content=".")])

#funcaion
query = sys.argv[1]

loader = GCSFileLoader(project_name="aist", bucket="testing-hwc", blob="fake.docx")
loader.load()

index = VectorstoreIndexCreator().from_loaders([loader])

#memory
from langchain import OpenAI, ConversationChain

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

conversation.run("Hi there!")

result =index.query(query ,llm=ChatOpenAI())
print(result.message.content)


# Streamlit app configuration
import streamlit as st
st.set_page_config(page_title="جباية", layout="wide")

# Writing the app main function
def main():

 # Setting up the app title and description
    st.title("")

st.write("Ask  question,  provide answers!")

# Available e types for the checklist
grope_types = ['اشتراك ', 'تسجيل دخول', 'اكمل كضيف']
# User selection for the type of places to visit
selected_types = st.multiselect("Select the type of ", grope_types)
if __name__ == "__main__":
    main()
