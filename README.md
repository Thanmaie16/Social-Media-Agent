# 📱 AI Social Media Agent

A Streamlit-powered AI tool that generates **content ideas**, **daily captions**, and **weekly content plans** for social media platforms using GPT-4o, Claude 3, or Gemini 1.5 Pro.

---

## 🚀 Features

### ✅ **AI-Powered Content Generation**

* 20 content ideas for any niche
* 10 daily captions with hashtags
* 7-day content planner with hooks + captions

### ✅ **Multi-Model Support**

Choose your preferred AI backend:

* **OpenAI GPT-4o**
* **Claude 3 Opus**
* **Gemini 1.5 Pro**

### ✅ **Vector Storage (Optional)**

Save generated results to **ChromaDB** for later retrieval.

### ✅ **Session Chat History**

Keeps track of conversations using Streamlit’s session state.

---

## 🛠️ Tech Stack

| Component     | Technology                          |
| ------------- | ----------------------------------- |
| Frontend      | Streamlit                           |
| AI Models     | OpenAI GPT-4o, Claude 3, Gemini 1.5 |
| Vector DB     | Chroma                              |
| Embeddings    | OpenAI Embeddings                   |
| Backend Logic | Python + LangChain                  |

---

## 📂 Project Structure

```
.
├── app.py
└── README.md
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ai-social-media-agent.git
cd ai-social-media-agent
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

*(If you don’t have a requirements file, create one with:)*

```
streamlit
langchain
langchain-openai
langchain-community
anthropic
google-generativeai
chromadb
```

---

## 🔐 API Keys Required

You must add credentials for at least one of the following:

* **OpenAI API Key**
* **Anthropic API Key**
* **Google Gemini API Key**

In Streamlit Cloud, add them under:
**Settings → Secrets → Add key**

Locally, you can export them:

```bash
export OPENAI_API_KEY="your_key"
export ANTHROPIC_API_KEY="your_key"
export GOOGLE_API_KEY="your_key"
```

---

## ▶️ Running the App

Start the Streamlit server:

```bash
streamlit run app.py
```

The app opens automatically in your browser:

```
http://localhost:8501/
```

---

## 📸 UI Overview

* Enter a content **topic / niche**
* Select **platform** (Instagram, TikTok, YouTube, LinkedIn)
* Select task:

  * Content Ideas
  * Daily Captions
  * Weekly Plan
* Choose AI model from the sidebar
* (Optional) Save results to vector DB

---

## 💾 Saving to Vector DB

When the "Save to Vector DB" checkbox is enabled, the generated output is stored into a **Chroma collection** for later retrieval or analysis.

---

## 🧩 Future Enhancements

* Add image generation for post thumbnails
* Auto-posting via Instagram / LinkedIn API
* Multi-user authentication
* Full analytics dashboard
* Hashtag performance predictor

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Show Your Support

If you found this helpful, don’t forget to **star the repository**! 🌟

---
