from fastapi import FastAPI
from pydantic import BaseModel
from chat_agent import chat_with_memory

app = FastAPI()

class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    reply = chat_with_memory(request.user_id, request.message)
    return {"reply": reply}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
