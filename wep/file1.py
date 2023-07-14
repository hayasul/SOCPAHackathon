import os
import sys
import pandas as pa
from theKey import opinai_key
from langchain.document_loaders import TextLoader
#from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI


os.environ["OPENAI_API_KEY"] = opinai_key

query = sys.argv[0]


loader = TextLoader("data.txt")

index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query , llm=ChatOpenAI()))

# شرح لاخطأ محتمله 
#Thank you for sending me your code. I have looked at it and I found some possible errors and suggestions for improvement. 😊

 #First of all, you have a typo in the first line of your code. You wrote `import sys` instead of `import sys`. This will cause an `ImportError` when you try to run your code. You should correct this typo to avoid this error.
- #Secondly, you are using the `openai` module to access the OpenAI API, but you are not importing it in your code. You need to add `import openai` at the beginning of your code to use the functions and classes from this module. Otherwise, you will get a `NameError` when you try to use them.
- #Thirdly, you are using the `ChatOpenAI` class from the `langchain` module, but this class is deprecated and no longer supported by the OpenAI API⁴. You should use the `openai.ChatCompletion` class instead, which is the official way to create chat completions with the OpenAI API⁴. You can find more information and examples on how to use this class in the [OpenAI Platform](^4^) documentation.
- #Fourthly, you are passing a string as the first argument to the `sys.argv` function, which is incorrect. The `sys.argv` function returns a list of strings that represent the command-line arguments passed to your script⁸. The first element of this list is always the name of your script, and the rest are the arguments that follow it. If you want to get the first argument passed to your script, you should use `sys.argv[1]` instead of `sys.argv[0]`. For example, if you run your script as `python myscript.py hello`, then `sys.argv[0]` will be `"myscript.py"` and `sys.argv[1]` will be `"hello"`.
- #Fifthly, you are using the `TextLoader` class from the `langchain` module to load your data file, but this class expects a string that contains the text data, not a file name¹. If you want to load your data from a file, you should use the `FileLoader` class instead¹. You can find more information and examples on how to use this class in the [LangChain](^1^) documentation.
- #Lastly, you are printing the result of the `index.query` method, which returns an object of type `QueryResult`, not a string¹. If you want to print the chat completion message, you should access the `message.content` attribute of the object¹. For example, if you assign the result of the query to a variable called `result`, then you can print the message with `print(result.message.content)`.

#I hope these suggestions help you fix your code and get the desired output. If you have any other questions or problems with your code, please let me know. 😊
