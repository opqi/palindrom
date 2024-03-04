from pydantic import BaseModel
from typing import Optional


class InputData(BaseModel):
    word: str


class OutputData(BaseModel):
    palindrome: Optional[str] = None
