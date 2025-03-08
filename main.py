from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class UserRequest(BaseModel):
    message: str

responses = {
    "kitty": "Here, take this: https://www.google.com/search?tbm=isch&q=kitties",
    "meaning of life": "Oh boy, I have no energy for this now. Look at this tree instead: 🌳",
    "poem": "Nah, not in the mood. Play this game instead: https://chromedino.com/",
}

@app.post("/chat")
async def chat(request: UserRequest):
    user_message = request.message.lower()
    
    # Return a predefined response or a default snarky reply
    for key in responses:
        if key in user_message:
            return {"response": responses[key]}
    
    return {"response": random.choice([
        "I don't care. Say something else.",
        "Ugh, do I look like Google?",
        "Not my problem.",
        "Ask better questions, human.",
    ])}
