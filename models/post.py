from typing import Optional
from pydantic import BaseModel


class Aur(BaseModel):

    name: str
    surname:str
    imag: str
    email: str


class Post(BaseModel):
    id: Optional[str]=""
    usr: Optional[str]
    mens: str
    imgs: Optional[str]
    autor: list[Aur] = None
