import asyncpg
import asyncio
from typing import List, Optional, Dict, Any

PG_HOST = "postgres"
PG_PORT = 5432
PG_USER = "bookstore_user"
PG_PASS = "BookstorePass456"
PG_DB = "bookstore_db"

_pool: Optional[asyncpg.pool.Pool] = None

async def get_pool():
    global _pool
    if _pool is None:
        _pool = await asyncpg.create_pool(
            host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASS, database=PG_DB, min_size=1, max_size=4
        )
    return _pool

async def fetch_books():
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT * FROM books")
        return [dict(r) for r in rows]

async def fetch_book_by_id(book_id: int):
    pool = await get_pool()
    async with pool.acquire() as conn:
        row = await conn.fetchrow("SELECT * FROM books WHERE id=$1", book_id)
        return dict(row) if row else None

async def fetch_books_by_author(author_id: int):
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT * FROM books WHERE author_id=$1", author_id)
        return [dict(r) for r in rows]

async def fetch_books_by_category(category_id: int):
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT * FROM books WHERE category_id=$1", category_id)
        return [dict(r) for r in rows]

async def insert_book(data: Dict[str, Any]):
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            """
            INSERT INTO books (title, description, publication_date, author_id, category_id)
            VALUES ($1, $2, $3, $4, $5)
            RETURNING *
            """,
            data["title"], data["description"], data["publication_date"], data["author_id"], data["category_id"]
        )

async def fetch_authors():
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT * FROM authors")
        return [dict(r) for r in rows]

async def fetch_categories():
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT * FROM categories")
        return [dict(r) for r in rows]
