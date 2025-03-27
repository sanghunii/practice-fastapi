import aiohttp 
import asyncio 

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()
    
async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",   
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        response = await asyncio.gather(*tasks)

        for i, response in enumerate(response):
            print(f"응답 {i + 1}: {response[:60]}...")


asyncio.run(main())