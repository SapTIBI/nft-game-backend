from src.services.user_service import UserService
from src.services.prize_service import PrizeService
from src.services.nft_service import NftService
from src.services.market_service import MarketService

from src.repositories.user import UserRepository
from src.repositories.prize import PrizeRepository
from src.repositories.nft import NftRepository
from src.repositories.market import MarketRepository

def users_service() -> UserService:
    return UserService(UserRepository)

def prizes_service() -> PrizeService:
    return PrizeService(PrizeRepository)

def nfts_service() -> NftService:
    return NftService(NftRepository)

def markets_service() -> MarketService:
    return MarketService(MarketRepository)