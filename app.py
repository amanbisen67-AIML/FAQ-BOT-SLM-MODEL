import streamlit as st

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from langchain_core.prompts import ChatPromptTemplate
# 1. Web Page Setup
st.title("Local FAQ Support Bot 🤖")
st.write("Ask me anything about our policies and services!")

# 2. Prepare the Knowledge Base (Cached so it only runs once)
@st.cache_resource
def setup_database():
    # Load the text file
    loader = TextLoader("faq_data.txt", encoding="utf-8")
    docs = loader.load()
    
    # Split the text into smaller, readable chunks
    # Split the text into smaller, readable chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = splitter.split_documents(docs)
    
    # Convert text to numbers and store in ChromaDB
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vector_store = Chroma.from_documents(split_docs, embeddings)
    
    # Return a retriever that fetches the most relevant chunk
    return vector_store.as_retriever()

retriever = setup_database()

# 3. Setup the AI Model and Instructions
llm = ChatOllama(model="phi3")

system_prompt = (
    "You are a professional banking and finance assistant. "
    "Use the following piece of context to answer the question. "
    "If the answer is not in the context, use your general knowledge about banking and finance ONLY. "
    "\n\nContext: {context}"
)

# We use Prompt Anchoring here by attaching the rule directly to the human input
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "User Question: {input}\n\nCRITICAL RULE: If the User Question above is about biology (like 'stomach'), anatomy, cooking, coding, sports, you MUST refuse to answer. Reply EXACTLY with: 'I am a specialized banking assistant and can only help you with finance-related inquiries.' Do not provide any facts about the non-financial topic."),
])

# Link the retrieval system to the AI generation system
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# 4. Chat Interface
user_input = st.text_input("Your Question:")

if user_input:
    with st.spinner("Searching records..."):
        # Run the query through the pipeline
        response = rag_chain.invoke({"input": user_input})
        
        # Display the AI's answer
        st.success("**Bot:** " + response["answer"])
