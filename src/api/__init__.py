from fastapi import APIRouter
from src.api.v1 import user, market, prize, nft

api_v1 = APIRouter(
    prefix="/api/v1"
)

api_v1.include_router(user.router)
api_v1.include_router(market.router)
api_v1.include_router(prize.router)
api_v1.include_router(nft.router)