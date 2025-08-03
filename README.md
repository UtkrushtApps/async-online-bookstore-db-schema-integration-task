# Task Overview

You are helping develop the backend for an online bookstore where users can add, list, and view books by authors and categories. The FastAPI application is completely set up with API routes, error handling, and project structure. Implementing an efficient and correct database layer is essential to ensure reliable book cataloging, prevent data inconsistency, and power all bookstore features.

## Guidance
- The FastAPI scaffolding, routers, and endpoint logic are fully implemented and working—the only missing component is a functional PostgreSQL database integration.
- Your main responsibilities are:
  - Define a robust, normalized schema in `schema.sql` to represent books, authors, and categories. Use correct foreign keys and relationships.
  - Populate `data/sample_data.sql` with at least five books, covering a variety of authors and categories.
  - Review the structure in `app/routes/api.py` and `app/database.py` to see how async DB access is expected—implement all async data-access logic using asyncpg, not synchronous libraries.
  - You do NOT need to edit, add, or understand API routing, serialization, or business logic. Focus only on database and async integration functions.
  - Ensure you are not blocking the event loop; all connection and query operations must be fully async.
- Recommended review order: Start with `schema.sql`, check expected structure in `schemas/`, then implement/complete utility functions in `app/database.py`.

## Database Access
- Host: `<DROPLET_IP>`
- Port: 5432
- Database: bookstore_db
- Username: bookstore_user
- Password: BookstorePass456
- Use any preferred client (pgAdmin, DBeaver, psql, etc.) to inspect and test the schema/data directly.

## Objectives
- Create PostgreSQL tables in `schema.sql` for books (with title, description, publication date, etc.), authors, categories, and establish all necessary relationships (e.g., each book belongs to one author and one category).
- Use correct data types, primary keys, unique/foreign constraints, and at least one index for optimized lookups.
- Populate `data/sample_data.sql` with at least five distinct books, representing multiple authors and categories.
- Implement async-compatible data-access logic (using asyncpg) in `app/database.py` for all CRUD and filter operations required by the existing routes.
- Ensure all FastAPI endpoints work as expected, returning book data with proper author/category info, and supporting asynchronous non-blocking operation.

## How to Verify
- On API startup, you should be able to list all books, filter books by author or category, and view single book details without server errors.
- Use HTTP clients (curl/Postman) or browsers to test all GET/POST endpoints; verify book/author/category info matches inserted database records.
- Use SQL tools to check your schema (tables, keys, constraints, sample data) and test performance with EXPLAIN on major queries.
- Confirm all async database logic (inserts, selects) runs without blocking the main FastAPI worker (run tests, check logs for errors or warnings about blocking calls).
