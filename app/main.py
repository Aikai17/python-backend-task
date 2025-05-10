"""App initialization"""
from fastapi import FastAPI
from app.routers import shortener
from app import database,models
from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.init_db()
    yield

app = FastAPI(title="URL Shortener", lifespan=lifespan)

app.include_router(shortener.router)

