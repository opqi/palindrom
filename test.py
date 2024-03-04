import asyncio
import aiohttp
import time

async def send_request(word):
    async with aiohttp.ClientSession() as session:
        url = "http://localhost:8000/palindrome"
        payload = {"word": word}
        start_time = time.time()
        async with session.post(url, json=payload) as response:
            data = await response.json()
            end_time = time.time()
            print(f"Response for '{word}': {data}")
            return end_time - start_time

async def main():
    with open('test_data.txt', 'r') as file:
        words = file.read().split()
    total_time = 0
    for word in words:
        total_time += await send_request(word)
    avg_time = total_time / len(words)
    print(f"Average request time: {avg_time} seconds")

asyncio.run(main())