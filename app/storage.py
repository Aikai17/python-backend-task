from .database import SessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import utils,models
async def save_url(db:AsyncSession,shortened_url:str,full_url:str):
    url=models.URL(short_url=shortened_url,full_url=full_url)
    db.add(url)
    try:
        await db.commit()
    except Exception as ex:
        print(ex)
        await db.rollback()

async def get_url(db:AsyncSession,shortened_url:str):
    result=await db.execute(select(models.URL).where(models.URL.short_url==shortened_url))
    url=result.scalars().first()
    if url:
        return url.full_url
    else:
        return None

