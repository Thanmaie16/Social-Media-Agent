import streamlit as st
from langchain_community.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True)

st.title("Memory Test")

msg = st.text_input("Message:")

if st.button("Add"):
    memory.chat_memory.add_user_message(msg)
    st.write(memory.load_memory_variables({}))
import streamlit as st
import datetime
from langchain_openai import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

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

# Initialize memory (optional)
memory = ConversationBufferMemory(return_messages=True)

# ---------------------------
# LLM SELECTOR
# ---------------------------
def load_model():
    if model_choice == "OpenAI GPT-4o":
        return ChatOpenAI(model_name="gpt-4o", temperature=0.8, api_key=api_key)

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
        return model.predict(prompt)

    elif model_choice == "Claude 3":
        return model.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        ).content[0].text

    elif model_choice == "Gemini 1.5":
        response = model.generate_content(prompt)
        return response.text

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
        st.stop()

    # -------------------------------------------------------------------
    # PROMPTS
    # -------------------------------------------------------------------
    if task == "Content Ideas":
        prompt = f"""
        Generate 20 unique content ideas for {platform} in the {topic} niche.
        Make them engaging, trend-driven, and high-performance.
        Format as bullet points.
        """

    elif task == "Daily Captions":
        prompt = f"""
        Create 10 Instagram captions for today's date ({datetime.date.today()}), 
        for the {topic} niche.

        Captions must be:
        - Short
        - Hook-based
        - Include trending hashtags
        """

    elif task == "Weekly Plan":
        prompt = f"""
        Create a weekly social media plan for {platform} in the {topic} niche.

        Include:
        - 7 days plan
        - Content type
        - Hook
        - Caption
        - Hashtags
        """

    # -------------------------------------------------------------------
    # GENERATE OUTPUT
    # -------------------------------------------------------------------
    with st.spinner("Generating..."):
        output = generate_response(prompt)

    st.success("Done!")
    st.write(output)

    # Save to vector DB (optional)
    if st.sidebar.checkbox("Save Output to Vector DB"):
        db = init_vector_db()
        db.add_texts([output])
        st.sidebar.success("Saved successfully!")

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("""
---
### 🚀 Tips for Deployment
- Save this file as `app.py`
- Deploy directly on **Streamlit Cloud**
- Add API keys through Streamlit **Secrets Manager**

---
""")
