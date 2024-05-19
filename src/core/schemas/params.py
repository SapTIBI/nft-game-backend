from pydantic import BaseModel

class Paginator(BaseModel):
    limit: int = 10
    offset: int = 0