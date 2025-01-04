from fastapi import FastAPI
app = FastAPI()

from starlette.middleware.cors import CORSMiddleware

##for openAI API 
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get('API_KEY')

origins = [
    'http://localhost:3001'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/chatBot')
async def chat():
    client = OpenAI(
        api_key=API_KEY
    )    
    
    ##Create Chat
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "나의 프롬프트 엔지니어링 코치가 되어줘."},
        {"role": "user", "content": "어떻게 하면 프롬프트 엔지니어링을 잘 할수 있을까?"}
    ]
    )
    ##parsing(get chatbot's answer)
    answer: str = response.choices[0].message.content
    
    
    return {'answer': answer}


""" 코드 설명
answer: str = response.choices[0].message.content.encode(encoding="utf-8").decode()

**reference**
https://chatgpt.com/share/6778fd12-d9cc-800b-ac1f-eeb0bd0b04f5
"""