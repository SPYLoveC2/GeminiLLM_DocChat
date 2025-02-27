import streamlit as st
import google.generativeai as genai
import os
import torch
from PyPDF2 import PdfReader
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_docling import DoclingLoader
from artifacts import checkfile_exist
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

torch.classes.__path__ = []
st.set_page_config(page_title='LLM powered Doc QA')
st.header("LLM powered Doc QA")

saved_file_path = None
do_emedding = None
file_name = None
retriever = None
def get_retriever(file_name):
    embedding = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    embedding_folder = os.path.join("./","embedding", file_name)
    db = FAISS.load_local(embedding_folder, embedding=embedding)
    retriever = db.as_retriever()
    return retriever



def get_available_embedding():
    lst = os.listdir("./embedding/")
    lst.remove('.gitkeep')
    print(lst)
    return lst


with st.sidebar:
    uploaded_file = st.file_uploader("Upload your file", accept_multiple_files=False)
    
    selfile = st.empty()
    selected_folder = selfile.selectbox('Select a file:', get_available_embedding(), index=None)
    
    if uploaded_file:
        selfile.empty()
        file_name = uploaded_file.name
        saved_file_path, do_emedding = checkfile_exist(uploaded_file)
        print(saved_file_path, do_emedding)

    elif selected_folder:
        file_name = selected_folder
        



def save_embedding(docs, file_name):
    embedding = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    placeholder = st.empty()
    placeholder.image("./webartifacts/progress.gif", use_container_width=True)
    db = FAISS.from_documents(docs, embedding=embedding)
    embedding_folder = os.path.join("./","embedding", file_name)
    os.makedirs(embedding_folder, exist_ok=True)
    db.save_local(folder_path=embedding_folder)
    placeholder.empty()
    st.write("Embedding Saved")


if saved_file_path and do_emedding=="YES":
    docs = None
    with st.sidebar:
        st.write("Document Processing")
        placeholder = st.empty()
        placeholder.image("./webartifacts/progress.gif", use_container_width=True)
        loader = DoclingLoader(saved_file_path)
        docs = loader.load()
        if len(docs) == 0:
            st.write("Invalid Doc Please check")
        placeholder.empty()
        st.write("Document Processed. \nEmbedding Started...")
        save_embedding(docs=docs, file_name=file_name)
        
        st.progress(100)
    

if selected_folder or do_emedding=="NO":
    retriever = get_retriever(file_name)