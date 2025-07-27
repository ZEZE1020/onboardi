import os
import google.generativeai as genai

# Configure once at import
genai.configure(api_key=os.getenv("GENAI_API_KEY", ""))

def execute(task: str, context: dict) -> str:
    """
    Send a single task to Gemini and return the assistant's reply.
    Raises ValueError on empty task.
    """
    if not task or not task.strip():
        raise ValueError("Task must be a non-empty string")

    prompt = (
        "You are a helpful AI assistant.\n"
        f"Task: {task}\n"
        "Respond concisely."
    )
    response = genai.chat.create(
        model="chat-bison-001",
        prompt=prompt
    )
    return response.last
