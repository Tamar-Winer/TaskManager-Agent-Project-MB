from fastapi import FastAPI
from pydantic import BaseModel
from agent_service import agent

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    # קריאה לסוכן שבנינו
    reply = agent(request.message)
    return {"reply": reply}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # מאפשר לכל קליינט להתחבר
    allow_methods=["*"],
    allow_headers=["*"],
)