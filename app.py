import streamlit as st
from transformers import pipeline
from sentence_transformers import SentenceTransformer
import pdfplumber
import os

# Set up constants
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL_NAME = "tiiuae/falcon-7b-instruct"

# Function to extract text from PDF
@st.cache_data
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Load models with caching
@st.cache_resource
def load_models():
    embedder = SentenceTransformer(EMBEDDING_MODEL)
    qa_pipeline = pipeline("text-generation", model=LLM_MODEL_NAME, device=-1)  # CPU fallback if no GPU
    return embedder, qa_pipeline

# Initialize models
embedder, qa_pipeline = load_models()

# Streamlit UI
st.title("Chat with PDF")
st.write("Upload a PDF and ask questions about its content using an AI model.")

# File uploader
pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])
if pdf_file is not None:
    with st.spinner("Processing PDF..."):
        pdf_text = extract_text_from_pdf(pdf_file)
    st.success("PDF processed successfully!")
    
    # Display extracted text
    st.subheader("Extracted Text from PDF")
    st.text_area("", pdf_text, height=300)

    # Question answering
    st.subheader("Ask a question about the PDF:")
    question = st.text_input("Type your question here:")
    if st.button("Submit"):
        if question:
            with st.spinner("Processing your question..."):
                # Embedding text (dummy)
                context = pdf_text[:1000]  # Limiting context to fit into model memory
                response = qa_pipeline(question, max_length=50, num_return_sequences=1)[0]["generated_text"]
            st.subheader("Answer:")
            st.write(response)
        else:
            st.warning("Please enter a question.")
