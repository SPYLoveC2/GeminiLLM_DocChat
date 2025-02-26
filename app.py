import streamlit as st
import google.generativeai as genai
import os

from PyPDF2 import PdfReader
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_docling import DoclingLoader
from artifacts import checkfile_exist

st.set_page_config(page_title='LLM powered Doc QA')
st.header("LLM powered Doc QA")

saved_file_path = None
do_emedding = None
with st.sidebar:
    uploaded_file = st.file_uploader("Select your files", accept_multiple_files=False)
    if uploaded_file:
        saved_file_path, do_emedding = checkfile_exist(uploaded_file)
        print(saved_file_path, do_emedding)
        
if saved_file_path and do_emedding:
    docs = None
    with st.sidebar:
        st.write("Document loading and chucking")
        docs = DoclingLoader(saved_file_path)
        st.progress(100)
    print(docs)

