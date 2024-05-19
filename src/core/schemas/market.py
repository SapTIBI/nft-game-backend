from pydantic import BaseModel

class MarketSchema(BaseModel):
    id: int
    name: str

class MarketCreateSchema(BaseModel):
    name:str

class MarketUpdateSchema(BaseModel):
    name: str