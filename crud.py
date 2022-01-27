from sqlalchemy.orm import Session

import models
import schemas
from shortener import get_random_scrap

def find_with_ordinary(db: Session, url: str):
        return db.query(models.LinkToLink) \
        .filter(models.LinkToLink.url == url) \
        .first()


def find_with_shortened(db: Session, shortenedUrl: str):
    return db.query(models.LinkToLink) \
        .filter(models.LinkToLink.shortenedUrl == shortenedUrl) \
        .first()


def shorten_link(db: Session, url: str):
    db_url_conformity = models.LinkToLink(
        url=url, shortenedUrl=get_random_scrap())
    db.add(db_url_conformity)
    db.commit()
    db.refresh(db_url_conformity)
    return db_url_conformity
