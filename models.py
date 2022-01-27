from sqlalchemy import Column, String, Integer

from database import Base

class LinkToLink(Base):
    __tablename__ = "linktolink"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    url = Column(String, index=True)
    shortenedUrl = Column(String, unique=True, index=True)
