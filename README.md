# Chat With Your PDF 📚🤖

This is a **Streamlit application** that enables you to chat with the content of a PDF file using state-of-the-art NLP techniques! With this app, you can upload a PDF file, ask questions about its content, and get intelligent answers in real time.

---

## Demo 🚀

### Screenshot:
![App Screenshot](assets/app-face.png "Chat With Your PDF Application")

### Video Tutorial:
You can follow this **video tutorial** to see how to set up and use the app!

[![Watch the video](assets/app-face.png)](assets/demo_tutorial.mp4)

*Alternative hosting:*  
If you cannot view the embedded video: [Download Video](https://drive.google.com/file/d/1OOKx3wXgWGxLGe0XEOtniDOl33mUtdHd/view?usp=sharing)  

---

## Features ✨

- 📓 **PDF Parsing:** Extracts content from PDF files for processing.
- 🤗 **Hugging Face Embeddings:** Utilizes advanced NLP embeddings using the `Instructor-based` model.
- 🔍 **Retrieval QA Pipeline:** Implements question-answering over your PDF content.
- 🛠 **Streamlit UI:** A friendly, interactive user interface for uploading PDFs and asking questions.
  
---

## Installation 🛠️

### 1. Clone the Repository
```bash
git clone https://github.com/FDC0178/chat-with-pdf.git
cd chat-with-pdf
```

### 2. Set Up a Python Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Secrets
Add the Hugging Face API key in your `secrets.toml` file:
```toml
[default]
HUGGINGFACEHUB_API_TOKEN = "your-huggingface-token"
```

Alternatively, set this in the **Streamlit Secrets** section (if hosted on Streamlit Cloud).

### 5. Run the Application
```bash
streamlit run app.py
```

---

## Usage 🖥️

1. Upload your **PDF file** via the file uploader.
2. Type in your **questions** in the text input box.
3. The app provides intelligent answers and extracts the relevant content from the PDF.

---

## Acknowledgments 🙏

We'd like to express our gratitude to the following resources for enabling this project:

- 🤗 [Hugging Face](https://huggingface.co/) for pre-trained NLP models.
- 📓 [LangChain](https://github.com/hwchase17/langchain) for retrieval-based NLP pipelines.
- 🎨 [Streamlit](https://streamlit.io/) for its easy-to-use app development framework.
- 🗂 [FAISS](https://faiss.ai/) for efficient similarity search and clustering.

---

## Resources 📖

Here are some helpful links related to the project:

- [Hugging Face Instructor-based Model Documentation](https://huggingface.co/hkunlp/instructor-base)
- [LangChain Documentation](https://python.langchain.com/en/latest/index.html)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)

---

## Contributing 🧬

We welcome contributions! Please fork the repo and make a pull request.

---

## License 📜

This project is licensed under the [MIT License](LICENSE).

---
