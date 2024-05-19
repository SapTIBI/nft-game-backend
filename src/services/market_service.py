from src.core.schemas.market import MarketCreateSchema, MarketUpdateSchema
from src.core.schemas.params import Paginator
from src.repositories.market import MarketRepository
from src.repositories.marketnft import MarketNftRepository

class MarketService:
    def __init__(self):
        self.market_repo = MarketRepository()
        self.marketnft_repo = MarketNftRepository()
    def create_market(self, market: MarketCreateSchema):
        market_dict = market.model_dump()
        market_id = self.market_repo.create_one(market_dict)
        return market_id

    def get_market(self, id: int):
        market = self.market_repo.get_one_by_id(id)
        return market.to_read_model()

    def get_markets(self, pagination: Paginator):
        pagination_dict = pagination.model_dump()
        markets = self.market_repo.get_all(pagination_dict)
        return markets

    def update_market(self, market_id: int, data: MarketUpdateSchema):
        update_market_dict = data.model_dump()
        updated_market = self.market_repo.update_one(market_id, update_market_dict)
        return updated_market.to_read_model()

    def delete_market(self, market_id: int):
        self.market_repo.delete_one(market_id)

    def get_nfts_for_market(self, market_id: int):
        self.marketnft_repo.get_nfts_for_market(market_id)