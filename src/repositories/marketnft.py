from src.core.database import get_db
from src.core.models.market import Market
from src.core.models.nft import Nft
from src.core.exceptions import MarketNotFoundException, MarketNotFoundException, NftNotFoundException
from sqlalchemy.exc import IntegrityError

class MarketNftRepository:
    def add_nft_for_market(self, market_id: int, nft_id: int):
        with get_db() as session:
            db_market = session.query(Market).filter(Market.id == market_id).first()
            if not db_market:
                raise MarketNotFoundException()
            db_nft = session.query(Nft).filter(Nft.id == nft_id).first()
            if not db_nft:
                raise NftNotFoundException()
            db_market.nfts.append(db_nft)
            session.commit()

    def get_nfts_for_market(self, market_id: int):
        with get_db() as session:
            db_market = session.query(Market).filter(Market.id == market_id).first()
            if not db_market:
                raise MarketNotFoundException()
            return db_market.nfts

    # def delete_nft_for_market(self, market_id: int, nft_id: int):
    #     with get_db() as session:
    #         db_market = session.query(Market).filter(Market.id == market_id).first()
    #         if not db_market:
    #             raise MarketNotFoundException()
    #         db_nft = session.query(Market).filter(Market.id == nft_id).first()
    #         if not db_nft:
    #             raise MarketNotFoundException()
    #         db_market.nfts.remove(db_nft)
    #         session.commit()