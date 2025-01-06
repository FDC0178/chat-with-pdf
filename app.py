import streamlit as st
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from sklearn.metrics.pairwise import cosine_similarity
import faiss

# Import configuration
from config import EMBEDDING_MODEL, LLM_MODEL_NAME, CHUNK_SIZE

# Load Models
@st.cache_resource
def load_models():
    embedder = SentenceTransformer(EMBEDDING_MODEL)
    qa_pipeline = pipeline("text-generation", model=LLM_MODEL_NAME, device=0)  # GPU if available
    return embedder, qa_pipeline

embedder, qa_pipeline = load_models()

# Helper: Extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Helper: Split text into chunks
def split_text_into_chunks(text, chunk_size=CHUNK_SIZE):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

# Helper: Generate FAISS index for embedding chunks
def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

# Streamlit App UI
st.title("Chat with PDF (Open Source Edition)")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file:
    with st.spinner("Extracting text from the PDF..."):
        text = extract_text_from_pdf(uploaded_file)
        st.success("Text extracted successfully!")
        st.text_area("Extracted Content:", text, height=200)

    # Split text and generate embeddings
    st.write("Processing the PDF...")
    chunks = split_text_into_chunks(text)
    embeddings = embedder.encode(chunks)
    index = create_faiss_index(embeddings)

    st.success("PDF content is ready for questions!")

    # Ask Questions
    st.write("Ask questions about the document:")
    question = st.text_input("Your question:")

    if question:
        # Embed the question and find the most relevant chunk
        question_embedding = embedder.encode([question])
        distances, indices = index.search(question_embedding, k=3)  # Top 3 relevant chunks

        # Generate context
        relevant_chunks = " ".join([chunks[idx] for idx in indices[0]])
        st.write("Context:")
        st.text_area("Relevant Content:", relevant_chunks, height=150)

        # Query the LLM
        st.write("Generating an answer...")
        response = qa_pipeline(
            f"Context: {relevant_chunks}\n\nQuestion: {question}\n\nAnswer:",
            max_length=200,
            temperature=0.7
        )
        st.write("Answer:")
        st.write(response[0]['generated_text'])

# Footer
st.caption("Powered by Streamlit, Hugging Face, FAISS, and Sentence Transformers.")