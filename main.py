from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import SessionLocal, engine
from shortener import check_availability

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"Hello": "World"}


@app.get("/find_shortened/")
def get_pair(url: str, db: Session = Depends(get_db)):
    relationship = crud.find_with_ordinary(db, url=url)
    return relationship

@app.get("/find_original/")
def get_pair(url: str, db: Session = Depends(get_db)):
    relationship = crud.find_with_shortened(db, shortenedUrl=url)
    return relationship

@app.get("/{shortenedUrl}/")
def get_link(shortenedUrl: str, db: Session = Depends(get_db)):
    relationship = crud.find_with_shortened(db, shortenedUrl=shortenedUrl)
    destination = relationship.url
    return RedirectResponse(destination)


@app.post("/shorten/")
def create_link(url_to_shorten: schemas.URL, db: Session = Depends(get_db)):
    if not check_availability(url_to_shorten.url):
        return {"Message": "The website is not available"}
    
    url_relationship = crud.find_with_ordinary(db, url=url_to_shorten.url)
    if url_relationship:
        return url_relationship
    return crud.shorten_link(db, url=url_to_shorten.url)