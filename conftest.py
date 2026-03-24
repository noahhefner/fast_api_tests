import sqlite3
import tempfile
import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.db import get_db


@pytest.fixture
def client():
    with tempfile.NamedTemporaryFile() as tmp:

        def override_get_db():
            conn = sqlite3.connect(tmp.name)
            conn.row_factory = sqlite3.Row
            try:
                yield conn
            finally:
                conn.close()

        conn = sqlite3.connect(tmp.name)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE items (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )
        """)

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

        app.dependency_overrides[get_db] = override_get_db

        with TestClient(app) as client:
            yield client

        app.dependency_overrides.clear()
