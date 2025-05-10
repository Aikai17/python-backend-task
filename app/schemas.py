"""Pydantic schemas to validate responses/requests"""

from pydantic import BaseModel

class UrlCreate(BaseModel):
    url: str