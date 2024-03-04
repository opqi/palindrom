from models import InputData, OutputData
from typing import Optional


async def count_char(word: str) -> dict:
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count 


async def is_palindrome_possible(word: str) -> bool:
    char_count = await count_char(word)

    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    
    return odd_count <= 1


async def get_palindrome(word: str) -> str:
    if not await is_palindrome_possible(word):
        return ''
    
    char_count = await count_char(word)
    
    left_half = ''
    odd_char = ''
    for char, count in sorted(char_count.items()):
        if count % 2 == 0:
            left_half += char * (count // 2)
        else:
            left_half += char * ((count - 1) // 2)
            odd_char = char
    
    right_half = left_half[::-1]
    
    if odd_char:
        return left_half + odd_char + right_half
    else:
        return left_half + right_half


async def check_palindrome(data: dict) -> dict:
    input_data = InputData(**data)
    word = input_data.word
    palindrome = await get_palindrome(word)
    return OutputData(palindrome=palindrome).dict()
