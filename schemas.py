from pydantic import BaseModel, AnyUrl

class URL(BaseModel):
    url: AnyUrl

class URLtoURL(BaseModel):
    url: str
    shortened_url: str