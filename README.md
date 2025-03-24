# 🤖 News AI

News AI is a fully automated, multi-agent system that curates, summarizes, and analyzes the latest AI-related news using LangChain, Groq LLMs, and real-time web scraping. With a single click, users get structured, insightful reports directly inside a modern Streamlit UI.

🔥 Live Demo
👉 Launch the app: https://ainews-ai.streamlit.app/

🧠 Features
With a single click, News AI scrapes the web for the latest AI news, organizes it into categories, and summarizes each article with:

✅ Headline
✅ Source & publish time
✅ A helpful snippet
✅ Full summary
✅ Future impact analysis
✅ Key insights
✅ Link to the original article

🧩 Architecture
+-------------------------+
|   User Clicks Button   |
+-----------+-------------+
            |
            ▼
+-------------------------+
|     Orchestrator Agent  | <-- Categorizes news
+-----------+-------------+
            |
            ▼
+-------------------------+
|     Worker Agents       | <-- Summarize, analyze, format
+-----------+-------------+
            |
            ▼
+-------------------------+
|   Synthesizer Node      | <-- Joins all reports
+-----------+-------------+
            |
            ▼
+-------------------------+
|     Streamlit UI        | <-- Displays final result
+-------------------------+

🚀 How to Run Locally
Clone the repo:
    git clone https://github.com/yourusername/news-ai.git

Install dependencies:
    uv sync

Set up .env file:
    GROQ_API_KEY=your_groq_key
    SERPER_API_KEY=your_serper_key
    LANGSMITH_API_KEY=your_langsmith_key
    LANGSMITH_PROJECT=NewsAI

Run the app:
    streamlit run main.py
