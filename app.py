import streamlit as st
from pdf_utils import extract_text_from_pdf
from groq import Groq

st.set_page_config(page_title="PDF Chatbot", layout="wide")
st.title("Chat with your PDF")

GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Reading PDF..."):
        st.session_state.pdf_text = extract_text_from_pdf(uploaded_file)
    st.success("PDF loaded! Ask your questions below.")

for i in range(0, len(st.session_state.messages), 2):
    user_msg = st.session_state.messages[i]
    with st.chat_message("user"):
        st.markdown(user_msg["content"])
    if i + 1 < len(st.session_state.messages):
        assistant_msg = st.session_state.messages[i + 1]
        with st.chat_message("assistant"):
            st.markdown(assistant_msg["content"])

if st.session_state.pdf_text:
    user_question = st.chat_input("Ask something about the document...")

    if user_question:
        with st.chat_message("user"):
            st.markdown(user_question)

        prompt = f"""
You are a helpful assistant. ONLY use the information provided in the document below to answer the user's question.

If the answer is not present in the document, respond with:
"I'm sorry, I couldn't find that information in the provided document."

Document:
\"\"\"
{st.session_state.pdf_text}
\"\"\"

Question: {user_question}
Answer:
"""

        response_text = ""
        with st.chat_message("assistant"):
            response_box = st.empty()
            with st.spinner("Thinking..."):
                completion = client.chat.completions.create(
                    model="meta-llama/llama-4-scout-17b-16e-instruct",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=1024,
                    stream=True,
                )
                for chunk in completion:
                    if chunk.choices[0].delta.content:
                        response_text += chunk.choices[0].delta.content
                        response_box.markdown(response_text)

        st.session_state.messages.append({"role": "user", "content": user_question})
        st.session_state.messages.append({"role": "assistant", "content": response_text})

        if len(st.session_state.messages) > 10:
            st.session_state.messages = st.session_state.messages[-10:]
