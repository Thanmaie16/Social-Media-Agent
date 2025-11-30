import streamlit as st
import datetime

# LLM Imports
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# FIXED memory imports
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.memory import ConversationBufferMemory

# Prompt Modules
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

# ---------------------------
# STREAMLIT UI SETUP
# ---------------------------
st.set_page_config(
    page_title="AI Social Media Agent",
    page_icon="📱",
    layout="wide"
)

st.title("📱 AI Social Media Agent")
st.write("Generate content ideas, captions & weekly plans.")

# Sidebar Settings
st.sidebar.header("⚙️ Configuration")

model_choice = st.sidebar.selectbox(
    "Choose your AI Model",
    ["OpenAI GPT-4o", "Claude 3", "Gemini 1.5"]
)

api_key = st.sidebar.text_input("Enter API Key", type="password")

task = st.sidebar.radio(
    "Select Task",
    ["Content Ideas", "Daily Captions", "Weekly Plan"]
)

# ---------------------------
# FIXED MEMORY
# ---------------------------
history = ChatMessageHistory()
memory = ConversationBufferMemory(chat_memory=history, return_messages=True)

# ---------------------------
# LLM SELECTOR
# ---------------------------
def load_model():
    if model_choice == "OpenAI GPT-4o":
        return ChatOpenAI(model="gpt-4o", temperature=0.8, api_key=api_key)

    elif model_choice == "Claude 3":
        from anthropic import Anthropic
        return Anthropic(api_key=api_key)

    elif model_choice == "Gemini 1.5":
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        return genai.GenerativeModel('gemini-1.5-pro')

# ---------------------------
# CORE AI FUNCTION
# ---------------------------
def generate_response(prompt):
    model = load_model()

    if model_choice == "OpenAI GPT-4o":
        return model.invoke(prompt).content

    elif model_choice == "Claude 3":
        resp = model.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=700,
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.content[0].text

    elif model_choice == "Gemini 1.5":
        resp = model.generate_content(prompt)
        return resp.text

# ---------------------------
# VECTOR DB (Optional)
# ---------------------------
def init_vector_db():
    embeddings = OpenAIEmbeddings(api_key=api_key)
    return Chroma(collection_name="ideas_db", embedding_function=embeddings)

# ---------------------------
# MAIN LOGIC
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    topic = st.text_input("Enter Your Niche / Topic (Example: Fitness, Fashion, AI, Coffee Shop):")

with col2:
    platform = st.selectbox("Select Platform", ["Instagram", "TikTok", "YouTube", "LinkedIn"])

submit = st.button("Generate")

if submit:
    if not api_key:
        st.error("Please enter API key.")
        st.stop()

    if not topic:
        st.warning("Please enter a topic.")
