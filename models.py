from sqlalchemy import Column, String

from database import Base

class LinkToLink(Base):
    __tablename__ = "linktolink"
    
    url = Column(String, primary_key=True, index=True)
    shortenedUrl = Column(String, unique=True, index=True)
