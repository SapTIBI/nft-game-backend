from pydantic import BaseModel

class PrizeSchema(BaseModel):
    id: int
    value: str

class PrizeCreateSchema(BaseModel):
    value: str

class PrizeUpdateSchema(BaseModel):
    value: str