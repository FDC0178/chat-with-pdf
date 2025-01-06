# Chat with PDF Application

This application allows you to upload a PDF file, extract its content, and ask questions about it using advanced NLP techniques powered by open-source models. Built with **Streamlit** for the user interface.

## Features

- Upload a PDF and view its extracted content.
- Perform efficient similarity-based queries using **Sentence-Transformers** and **FAISS**.
- Ask questions about the document, with answers generated using a **GPT-J** or similar model from Hugging Face.
- Fully open-source pipeline.

## Installation

### Prerequisites

- Python 3.8 or higher.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chat-with-pdf.git
   cd chat-with-pdf
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501`.

## Usage

1. Upload a PDF document.
2. Wait for the text to be extracted and processed.
3. Enter a question related to the document.
4. View the answer and relevant context.

## Acknowledgments

This application uses the following tools and frameworks:

- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [Sentence Transformers](https://www.sbert.net/)
- [FAISS](https://faiss.ai/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)

## License

MIT License. See `LICENSE` for details.