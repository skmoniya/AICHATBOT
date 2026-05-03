import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

client = Groq(api_key="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")

st.title("🤖 AI Chatbot")

# Role selection
role = st.selectbox("Choose Assistant Type", ["Tutor", "Friend", "Coder"])

system_prompt = {
    "Tutor": "You explain concepts clearly like a teacher.",
    "Friend": "You talk casually like a friendly buddy.",
    "Coder": "You are an expert programming assistant."
}[role]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

# Display previous messages
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # AI response
    response = client.chat.completions.create(
         model="llama-3.1-8b-instant",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)

# Reset button
if st.button("Reset Chat"):
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]