import os
import streamlit as st
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader
import torch

# Constants
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # Smaller and efficient embedding model
LLM_MODEL_NAME = "distilgpt2"  # Lightweight LLM for text generation

# Load models function
@st.cache_resource
def load_embedder():
    """
    Load the SentenceTransformer embedder for embeddings.
    """
    st.write("Loading embedding model...")
    try:
        embedder = SentenceTransformer(EMBEDDING_MODEL)
        st.write("Embedder loaded successfully!")
        return embedder
    except Exception as e:
        st.error(f"Failed to load embedder: {str(e)}")
        return None


@st.cache_resource
def load_qa_pipeline():
    """
    Load the QA pipeline using Hugging Face transformers.
    """
    st.write("Loading LLM model...")
    try:
        # Use CPU (-1) as Streamlit Cloud likely lacks GPU support
        qa_pipeline = pipeline("text-generation", model=LLM_MODEL_NAME, device=-1)
        st.write("LLM model loaded successfully!")
        return qa_pipeline
    except Exception as e:
        st.error(f"Failed to load LLM model: {str(e)}")
        return None


def process_pdf(file):
    """
    Extract text from uploaded PDF file.
    """
    try:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return None


# Streamlit app layout
st.title("Chat with PDF")
st.write("Upload a PDF and ask questions about its content using a lightweight AI model.")

# File upload
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file is not None:
    st.write("Processing PDF...")
    pdf_content = process_pdf(uploaded_file)

    if pdf_content:
        st.text_area("Extracted Text from PDF", pdf_content, height=300)
        
        # Load models
        embedder = load_embedder()
        qa_pipeline = load_qa_pipeline()

        if embedder and qa_pipeline:
            # User question input
            question = st.text_input("Ask a question about the PDF:")
            if question:
                # Dummy QA Implementation (Since GPT-2 lacks QA capability, adjust here)
                # In a proper setup, we'd replace this with a full QA pipeline like BERT-QA
                st.write("Processing your question...")
                try:
                    embeddings = embedder.encode(pdf_content)
                    answer = qa_pipeline(question)[0]["generated_text"]
                    st.write("Answer:", answer)
                except Exception as e:
                    st.error(f"Error generating answer: {str(e)}")
        else:
            st.error("Failed to load required models.")
else:
    st.info("Upload a PDF to get started!")
