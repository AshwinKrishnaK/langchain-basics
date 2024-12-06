from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes
import uvicorn

load_dotenv()

llm = ChatGroq(model='gemma2-9b-it',groq_api_key=os.getenv('groq_api_key'))
prompt = ChatPromptTemplate.from_messages(
    [("system","Translate following from English to {language}"),
     ("user","{text}")]
)
parser=StrOutputParser()
chain = prompt|llm|parser

result = chain.invoke({"language":"Malayalam","text":"Hello how are you"})
print(result)
app = FastAPI(title='Langchain server',
              version=1.0,
              description="Simple API for Langchain")

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ =="__main__":
    uvicorn.run(app,host="127.0.0.1", port=8000)
