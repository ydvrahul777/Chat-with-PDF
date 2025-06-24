# 📄 Chat with PDF using LLaMA-4 

This is a simple and fast chatbot app that lets you **upload any PDF** and **ask questions about its content** using the **Groq API + LLaMA-4 Scout 17B model**.

The app is built using **Streamlit** and deployed publicly on Streamlit Cloud.

---

## 🚀 Demo

🔗 [Click here to try the app](https://chat-with-pdf-07.streamlit.app/)

> Upload a PDF and ask questions like:
> - "What is this document about?"
> - "Who is the author?"
> - "Summarize section 2"

---

## 🧠 Features

- 📤 Upload any PDF (multi-page supported)
- 💬 Ask natural language questions
- 🦙 Uses **Groq’s LLaMA-4 Scout 17B** for fast, high-quality answers
- 🔐 Doesn’t guess — answers only based on PDF content
- 💬 Keeps the last **5 Q&A pairs** in memory
- 🌐 Deployable to **Streamlit Cloud** with your own API key

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — UI framework
- [Groq API](https://console.groq.com/) — LLM backend
- [LLaMA-4 Scout 17B](https://groq.com) — fast and accurate LLM
- [pdfplumber](https://github.com/jsvine/pdfplumber) — PDF text extraction

---

## 📦 Local Setup

1. **Clone the repo:**

```bash
git clone https://github.com/ydvrahul777/Chat-with-PDF.git
cd Chat-with-PDF
