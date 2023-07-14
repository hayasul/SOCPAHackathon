import os
import sys
import pandas as pa
from theKey import opinai_key
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI


os.environ["OPENAI_API_KEY"] = opinai_key

query = sys.argv[0]


loader = TextLoader("data.txt")

index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query , llm=ChatOpenAI()))

