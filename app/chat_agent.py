import redis
import openai
import os

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def chat_with_memory(user_id, message):
    history = r.get(user_id) or ""
    prompt = f"{history}\nUser: {message}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    answer = response.choices[0].text.strip()
    updated_history = f"{history}\nUser: {message}\nAI: {answer}"
    r.set(user_id, updated_history)
    return answer
