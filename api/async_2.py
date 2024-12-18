##잘못된 async사용
##두개의 req.py를 실행 시켜서 각각의 프로세스가 async_1.py를 실행 했을 때와 어떻게 다른지 보라

from fastapi import FastAPI
import asyncio

async def some_library(num: int, something: str):
    s = 0
    for i in range(num):
        print(" somthing .. : ", something, i)
        await asyncio.sleep(1) ##asyncio.sleep()은 non-block형식임
        s += int(something)
    return s

app = FastAPI()

@app.post('/')
async def read_results(something: str):
    s1 = await some_library(5, something)
    return {'data': 'data', 's1': s1}
