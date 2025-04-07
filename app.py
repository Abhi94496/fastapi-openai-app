from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
load_dotenv() 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = FastAPI()
class querypayload(BaseModel):
    query : str

@app.post("/query")
async def query(payload : querypayload):
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": payload.query}])
    return {"response" : response.choices[0].message.content}