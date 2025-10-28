# app.py
import streamlit as st
from main import get_response

# --- Page Configuration ---
st.set_page_config(page_title="Kuve Support Assistant 🤖", page_icon="💬", layout="centered")

# --- Title & Description ---
st.title("💬 Kuve Support Assistant")
st.write("Hi there! I’m **Kuve’s FAQ bot**. Ask me anything about Kuve’s features, setup, or troubleshooting — I’ll remember our chat context to give you precise answers.")

# --- Initialize memory ---
if "history" not in st.session_state:
    st.session_state.history = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display previous chat messages ---
for msg in st.session_state.messages:
    role = "🧑‍💬 You" if msg["role"] == "user" else "🤖 Kuve Bot"
    st.chat_message(msg["role"]).markdown(f"**{role}:** {msg['content']}")

# --- Chat input ---
user_input = st.chat_input("Ask something about Kuve...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(f"**🧑‍💬 You:** {user_input}")

    # Get model response
    with st.spinner("Thinking..."):
        response, updated_history = get_response(user_input, st.session_state.history)

    # Display assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(f"**🤖 Kuve Bot:** {response}")

    # Update conversation memory
    st.session_state.history = updated_history
