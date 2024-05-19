from src.core.database import get_db
from src.core.models.nft import Nft
from src.core.models.market import Market
from src.repositories.meta import AbstractRepository
from src.core.exceptions import NftAlreadyExistException, NftNotFoundException, MarketNotFoundException
from sqlalchemy.exc import IntegrityError

class NftRepository(AbstractRepository):
    def create_one(self, data: dict) -> int:
        with get_db() as session:
            try:
                market_id = data.get('market_id')
                db_nft = session.query(Market).filter(Market.id == market_id).first()
                if not db_nft:
                    raise MarketNotFoundException()
                db_object = Nft(**data)
                session.add(db_object)
                session.commit()
                session.refresh(db_object)
            except IntegrityError as e:
                print(e)
                raise NftAlreadyExistException()
            return db_object.id
            
    def get_one_by_id(self, id: int):
        with get_db() as session:
            db_object = session.query(Nft).filter_by(id=id).first()
            if not db_object:
                raise NftNotFoundException()
            return db_object
            
    def get_all(self, pagination: dict):
        limit = pagination.get('limit')
        offset = pagination.get('offset')
        with get_db() as session:
            db_object = session.query(Nft).limit(limit).offset(offset).all()
            return db_object
    
    def update_one(self, id: int, data: dict):
        with get_db() as session:
            try:
                db_object = session.query(Nft).filter_by(id=id).first()
                if not db_object:
                    raise NftNotFoundException()
                for key, value in data.items():
                    setattr(db_object, key, value)
                session.commit()
            except IntegrityError:
                raise NftAlreadyExistException()
            session.refresh(db_object)
            return db_object
    
    def delete_one(self, id: int):
        with get_db() as session:
            db_object = session.query(Nft).filter_by(id=id).first()
            if not db_object:
                raise NftNotFoundException()
            session.delete(db_object)
            session.commit()
        