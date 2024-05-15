from pydantic import BaseModel

class STaskAdd(BaseModel):
   name: str
   description: str | None = None


# class PrizeCreateDTO(BaseModel):
#    value: int


class PrizeCreateDTO(BaseModel):
   value: int

class PrizeUpdateDTO(BaseModel):
   value: int

class UserCreateDTO(BaseModel):
   username: str
   tgToken: str
   email: str

class UserUpdateDTO(BaseModel):
   username: str
   tgToken: str
   role: str
   email: str
   balance: int
   refScore: int


class UserPrizeCreateDTO(BaseModel):
   user_id: int
   prize_id: int

class UserPrizeDeleteDTO(BaseModel):
   user_id: int
   prize_id: int


class UserNftCreateDTO(BaseModel):
   user_id: int
   nft_id: int

class UserNftDeleteDTO(BaseModel):
   user_id: int
   nft_id: int

class NftCreateDTO(BaseModel):
   market_id: int
   name: str
   workBalance: int
   price: int

class NftUpdateDTO(BaseModel):
   name: str
   workBalance: int
   price: int


class MarketCreateDTO(BaseModel):
   name: str

class MarketUpdateDTO(BaseModel):
   name: str