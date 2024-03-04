from fastapi import FastAPI
from services import check_palindrome


app = FastAPI()


@app.post('/palindrome')
async def palindrome_endpoint(data: dict):
    return await check_palindrome(data)
