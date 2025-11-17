import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Fetch API key from .env
api_version = os.getenv("API_VERSION")
endpoint = os.getenv("ENDPOINT")
api_key =os.getenv("SUBSCRIPTION_KEY")
deployment = os.getenv("DEPLOYMENT")

if api_key is None:
    st.error("API key not found! Make sure OPENAI_API_KEY is in your .env file.")
else:
    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        api_key=api_key,
    )

st.title("Chatbot using OpenAI gpt-4.1-mini with Memory")
st.write("Ask me anything. I remember our past conversation!")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def get_model_response(chat_history):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history,
        temperature=0.7
    )
    return response.choices[0].message.content

user_prompt = st.text_input("You:", placeholder="Type your message here...")

if user_prompt:
    # Add user message to memory
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Get response from GPT
    assistant_response = get_model_response(st.session_state.chat_history)

    # Add assistant reply to memory
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

# Display chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**Chatbot:** {chat['content']}")

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.chat_history = []

