import streamlit as st
import datetime
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate

# --------------------------------------------------
# STREAMLIT PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AI Social Media Agent",
    page_icon="📱",
    layout="wide"
)

st.title("📱 AI Social Media Agent")
st.write("Generate content ideas, daily captions, and weekly plans using AI.")

# --------------------------------------------------
# STREAMLIT SESSION MEMORY (REPLACES LangChain Memory)
# --------------------------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def add_history(role, message):
    st.session_state.chat_history.append({"role": role, "message": message})

# --------------------------------------------------
# SIDEBAR SETTINGS
# --------------------------------------------------
st.sidebar.header("⚙️ Configuration")

model_choice = st.sidebar.selectbox(
    "Choose AI Model",
    ["OpenAI GPT-4o", "Claude 3 Opus", "Gemini 1.5 Pro"]
)

api_key = st.sidebar.text_input("Enter API Key", type="password")

task = st.sidebar.radio(
    "Select Task",
    ["Content Ideas", "Daily Captions", "Weekly Plan"]
)

# --------------------------------------------------
# LLM LOADER
# --------------------------------------------------
def load_model():
    if model_choice == "OpenAI GPT-4o":
        return ChatOpenAI(
            api_key=api_key,
            model="gpt-4o",
            temperature=0.8
        )

    elif model_choice == "Claude 3 Opus":
        from anthropic import Anthropic
        return Anthropic(api_key=api_key)

    elif model_choice == "Gemini 1.5 Pro":
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        return genai.GenerativeModel("gemini-1.5-pro")

# --------------------------------------------------
# GENERATE RESPONSE
# --------------------------------------------------
def generate_response(prompt):
    model = load_model()

    add_history("user", prompt)

    if model_choice == "OpenAI GPT-4o":
        response = model.invoke(prompt).content
        add_history("assistant", response)
        return response

    elif model_choice == "Claude 3 Opus":
        response = model.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=700,
            messages=[{"role": "user", "content": prompt}]
        )
        text = response.content[0].text
        add_history("assistant", text)
        return text

    elif model_choice == "Gemini 1.5 Pro":
        response = model.generate_content(prompt)
        add_history("assistant", response.text)
        return response.text

# --------------------------------------------------
# VECTOR DB (OPTIONAL)
# --------------------------------------------------
def init_vector_db():
    embeddings = OpenAIEmbeddings(api_key=api_key)
    return Chroma(collection_name="ideas_db", embedding_function=embeddings)

# --------------------------------------------------
# MAIN APP UI
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    topic = st.text_input("Enter Niche / Topic (e.g., Fitness, AI, Coffee Shop):")

with col2:
    platform = st.selectbox("Platform", ["Instagram", "TikTok", "YouTube", "LinkedIn"])

submit = st.button("Generate")

# --------------------------------------------------
# PROMPT GENERATION
# --------------------------------------------------
if submit:

    if not api_key:
        st.error("Please enter your API key.")
        st.stop()

    if not topic:
        st.warning("Please enter a topic.")
        st.stop()

    if task == "Content Ideas":
        prompt = f"""
        Generate 20 content ideas for {platform} in the {topic} niche.
        Make them engaging and trend-driven. Use bullet points.
        """

    elif task == "Daily Captions":
        prompt = f"""
        Write 10 Instagram captions for {topic} for today's date ({datetime.date.today()}).
        Captions must be short, hook-based, and include trending hashtags.
        """

    elif task == "Weekly Plan":
        prompt = f"""
        Create a 7-day {platform} content plan for the {topic} niche.
        Include:
        - Content type
        - Hook
        - Caption
        - Hashtags
        """

    with st.spinner("Generating..."):
        output = generate_response(prompt)

    st.success("Done!")
    st.write(output)

    # Save to vectorDB
    if st.sidebar.checkbox("Save to Vector DB"):
        db = init_vector_db()
        db.add_texts([output])
        st.sidebar.success("Saved!")

# --------------------------------------------------
# CHAT HISTORY (using Streamlit memory only)
# --------------------------------------------------
with st.expander("📜 Chat History"):
    for chat in st.session_state.chat_history:
        st.write(f"**{chat['role'].title()}:** {chat['message']}")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
---
### 📌 Deployment Tips
- Save this file as **app.py**
- Deploy on **Streamlit Cloud**
- Add API keys in **Settings → Secrets**
---
""")
