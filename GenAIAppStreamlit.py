import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.retrieval import create_retrieval_chain

load_dotenv()
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')
os.environ['LANGCHAIN_TRACING_V2'] = "true"

text_splitter = RecursiveCharacterTextSplitter(chunk_size=400,chunk_overlap=100)
documents = PyPDFLoader(file_path='AI_Agents_Benefits.pdf').load_and_split(text_splitter)

embedding = OpenAIEmbeddings(model='text-embedding-3-small')
vector_store = FAISS.from_documents(documents,embedding)

llm = ChatOpenAI(model="gpt-4o")
result = vector_store.similarity_search("What are benifits of AI")
retriver = vector_store.as_retriever()

prompt = ChatPromptTemplate.from_template(
    """
    Based on the context provided, answer the question concisely and accurately. If the context does not contain enough information, respond with "I don't know".    <context>
    {context}
    </context>
    """
)

document_chain = create_stuff_documents_chain(llm,prompt)

response = document_chain.invoke({
    "input":"What are benefits of AI. Explain in details",
    "context": result
})
print("Response from document chain")
print(response)
retriever_chain = create_retrieval_chain(retriver,document_chain)
response = retriever_chain.invoke({
    "input":"What are benefits of AI. Explain in details"
})
print("Response from retriever chain")
print(response['answer'])