"""Main route for shortening URL"""

from fastapi import APIRouter,Depends,status,HTTPException, Response
from fastapi.responses import RedirectResponse
from .. import schemas,utils,database,storage

router = APIRouter(tags=["URL_Shortener"])

@router.post('/',status_code=status.HTTP_201_CREATED)
async def shorten_url(url: schemas.UrlCreate,db=Depends(database.get_db)):
    shortened=utils.generate_short_url(url.url)
    await storage.save_url(db,shortened_url=shortened,full_url=url.url)
    return {"URL":shortened}

@router.get('/{short_url}',status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def shortened_url(short_url:str,db=Depends(database.get_db)):
    full_url = await storage.get_url(db,shortened_url=short_url)
    if not full_url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="URL Was not found")
    return RedirectResponse(full_url)

