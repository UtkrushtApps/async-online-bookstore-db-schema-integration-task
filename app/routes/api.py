from fastapi import APIRouter, HTTPException
from app.schemas import schemas
from app import database
from typing import List

router = APIRouter()

@router.get("/books", response_model=List[schemas.Book])
async def list_books():
    books = await database.fetch_books()
    return books

@router.get("/books/{book_id}", response_model=schemas.Book)
async def get_book(book_id: int):
    book = await database.fetch_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.get("/authors", response_model=List[schemas.Author])
async def list_authors():
    return await database.fetch_authors()

@router.get("/categories", response_model=List[schemas.Category])
async def list_categories():
    return await database.fetch_categories()

@router.get("/authors/{author_id}/books", response_model=List[schemas.Book])
async def list_books_by_author(author_id: int):
    return await database.fetch_books_by_author(author_id)

@router.get("/categories/{category_id}/books", response_model=List[schemas.Book])
async def list_books_by_category(category_id: int):
    return await database.fetch_books_by_category(category_id)

@router.post("/books", response_model=schemas.Book, status_code=201)
async def create_book(book: schemas.BookCreate):
    result = await database.insert_book(book.dict())
    if result is None:
        raise HTTPException(status_code=400, detail="Book could not be created")
    return dict(result)
