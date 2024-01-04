import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

st.title("Enchanting Chatbot 🌟")

question = st.text_input("Ask me anything: ✨")

if question:
    # Fetch the magical QA chain
    chain = get_qa_chain()

    # Cast a spell to get the answer
    response = chain(question)

    st.header("🔮 Mystical Answer")
    
    # Unveil the magical response
    st.write(f"🧙‍♂️ {response['result']} 🧙‍♀️")






