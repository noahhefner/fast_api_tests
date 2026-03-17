import os
import sqlite3
from contextlib import asynccontextmanager  # or just contextmanager if synchronous

from fastapi import FastAPI

from src.routers.domains import items

DATABASE_PATH = "test.db"


def init_db():
    # 1. Delete existing DB file
    if os.path.exists(DATABASE_PATH):
        os.remove(DATABASE_PATH)

    # 2. Create new DB + schema
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE items (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)

    # 3. Insert test data
    test_data = [
        ("11111111-1111-1111-1111-111111111111", "Apples", 10),
        ("22222222-2222-2222-2222-222222222222", "Bananas", 25),
        ("33333333-3333-3333-3333-333333333333", "Oranges", 15),
    ]

    cursor.executemany(
        "INSERT INTO items (id, name, quantity) VALUES (?, ?, ?)", test_data
    )

    conn.commit()
    conn.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    init_db()
    yield
    # Shutdown logic (if needed)
    # e.g., close DB connections, clean up resources


app = FastAPI(
    title="FastAPI Test Repo Structure",
    description="API for testing new repo structure.",
    version="0.1.0",
    lifespan=lifespan,  # attach the lifespan context manager
)

app.include_router(items.router)
