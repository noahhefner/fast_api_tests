from fastapi import FastAPI

from src.routers import items, orders

app = FastAPI(
    title="FastAPI Test Repo Structure",
    description="API for testing new repo structure.",
    version="0.1.0",
)

app.include_router(
    items.router,
)

app.include_router(
    orders.router,
)
