from fastapi import FastAPI
app = FastAPI()

from starlette.middleware.cors import CORSMiddleware

##for openAI API 
from openai import OpenAI
from dotenv import load_dotenv
import os

##for Streaming Response
from fastapi.responses import StreamingResponse

load_dotenv()
API_KEY = os.environ.get('API_KEY')

origins = [
    'http://localhost:3000',
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
    stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "나의 프롬프트 엔지니어링 코치가 되어줘."},
        {"role": "user", "content": "어떻게 하면 프롬프트 엔지니어링을 잘 할수 있을까?"}
    ],
    stream=True
    )
    ##parsing(get chatbot's answer)
    
    async def stream_response():
        for chunck in stream:
            if chunck.choices[0].delta.content is not None:
                yield chunck.choices[0].delta.content
    
    return StreamingResponse(stream_response(), media_type = "text/plain")


   ##return {'anser' : chunck.choices[0].delta.content} 



"""
# 스트리밍 응답 생성
    async def stream_response():
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content
    
    return StreamingResponse(stream_response(), media_type="text/plain")
"""