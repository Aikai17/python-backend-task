"""ORM models"""
from sqlalchemy import Column, Integer, String

from .database import Base

class URL(Base):
    __tablename__='Urls'
    id=Column(Integer,primary_key=True)
    short_url=Column(String,nullable=False)
    full_url=Column(String,nullable=False)