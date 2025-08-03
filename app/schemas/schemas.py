from pydantic import BaseModel
from typing import Optional
from datetime import date

class Author(BaseModel):
    id: int
    name: str
    bio: Optional[str]

class Category(BaseModel):
    id: int
    name: str
    description: Optional[str]

class Book(BaseModel):
    id: int
    title: str
    description: Optional[str]
    publication_date: date
    author_id: int
    category_id: int

class BookCreate(BaseModel):
    title: str
    description: Optional[str]
    publication_date: date
    author_id: int
    category_id: int
