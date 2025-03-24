from langchain_groq import ChatGroq
from news_ai.schema import Sections
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

llm = ChatGroq(model="gemma2-9b-it")

# Augment the LLM with schema for structured output
planner = llm.with_structured_output(Sections)
