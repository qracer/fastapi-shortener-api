from sqlalchemy.orm import Session

import models
# import schemas
from shortener import shorten


def find_with_ordinary(db: Session, url: str):
    """Find a shortened version in the database by an original URL"""
    return db.query(models.LinkToLink) \
        .filter(models.LinkToLink.url == url) \
        .first()


def find_with_shortened(db: Session, shortenedUrl: str):
    """Find an original URL in the database by a shortened version"""
    return db.query(models.LinkToLink) \
        .filter(models.LinkToLink.shortenedUrl == shortenedUrl) \
        .first()


def shorten_link(db: Session, url: str):
    """Generate a contraction and add a received pair to the database"""
    db_url_conformity = models.LinkToLink(
        url=url, shortenedUrl=shorten(url))
    db.add(db_url_conformity)
    db.commit()
    db.refresh(db_url_conformity)
    return db_url_conformity


def create_link(db: Session, url: str, shortUrl: str):
    """Add a prepared pair to the database"""
    db_url_conformity = models.LinkToLink(
        url=url, shortenedUrl=shortUrl)
    db.add(db_url_conformity)
    db.commit()
    db.refresh(db_url_conformity)
    return db_url_conformity
