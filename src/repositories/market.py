from src.core.database import get_db
from src.core.models.market import Market
from src.repositories.meta import AbstractRepository
from src.core.exceptions import MarketAlreadyExistException, MarketNotFoundException
from sqlalchemy.exc import IntegrityError

class MarketRepository(AbstractRepository):
    def create_one(self, data: dict) -> int:
        with get_db() as session:
            try:
                db_object = Market(**data)
                session.add(db_object)
                session.commit()
                session.refresh(db_object)
            except IntegrityError:
                raise MarketAlreadyExistException()
            return db_object.id
            
    def get_one_by_id(self, id: int):
        with get_db() as session:
            db_object = session.query(Market).filter_by(id=id).first()
            if not db_object:
                raise MarketNotFoundException()
            return db_object
            
    def get_all(self, pagination: dict):
        limit = pagination.get('limit')
        offset = pagination.get('offset')
        with get_db() as session:
            db_object = session.query(Market).limit(limit).offset(offset).all()
            return db_object
    
    def update_one(self, id: int, data: dict):
        with get_db() as session:
            try:
                db_object = session.query(Market).filter_by(id=id).first()
                if not db_object:
                    raise MarketNotFoundException()
                for key, value in data.items():
                    setattr(db_object, key, value)
                session.commit()
            except IntegrityError:
                raise MarketAlreadyExistException()
            session.refresh(db_object)
            return db_object
    
    def delete_one(self, id: int):
        with get_db() as session:
            db_object = session.query(Market).filter_by(id=id).first()
            if not db_object:
                raise MarketNotFoundException()
            session.delete(db_object)
            session.commit()
        