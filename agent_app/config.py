
import os
from dotenv import load_dotenv
from langchain_community.llms import OpenAI

load_dotenv()

def get_llm():
    os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE_VLLM")
    return OpenAI(
        model_name=os.getenv("OPENAI_MODEL_VLLM", "vllm-fork-with-llama-2-7b-chat-hf"),
        max_tokens=128,
        temperature=0
    )

def get_openweather_api_key():
    return os.getenv("OPENWEATHER_API_KEY")
