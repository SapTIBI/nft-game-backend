from pydantic import BaseModel

class NftSchema(BaseModel):
    id:int
    name:str
    workBalance:int
    price:int
    market_id: int
    
class NftCreateSchema(BaseModel):
    name:str
    workBalance:int
    price:int
    market_id: int

class NftUpdateSchema(BaseModel):
    name:str
    workBalance:int
    price:int