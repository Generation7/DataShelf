from fastapi import FastAPI
from .routers import items


app = FastAPI(title="FastAPI + SQLite Example")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


app.include_router(items.router, prefix="/items", tags=["items"])


