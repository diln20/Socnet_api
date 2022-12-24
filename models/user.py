from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str]
    name: str
    surname: Optional[str]
    email: str
    password: str
    imag: Optional[str]
