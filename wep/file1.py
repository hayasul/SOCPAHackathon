import os
import sys

import constant
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constant.APIKEY

query = sys.argv[0]

#تعديل
print("hiiii")
loader = TextLoader("data.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query , llm=ChatOpenAI()))

