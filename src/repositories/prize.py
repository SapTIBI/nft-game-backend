from src.core.database import get_db
from src.core.models.prize import Prize
from src.repositories.meta import AbstractRepository
from src.core.exceptions import PrizeAlreadyExistException, PrizeNotFoundException
from sqlalchemy.exc import IntegrityError

class PrizeRepository(AbstractRepository):
    def create_one(self, data: dict) -> int:
        with get_db() as session:
            try:
                db_object = Prize(**data)
                session.add(db_object)
                session.commit()
                session.refresh(db_object)
                return db_object.id
            except IntegrityError:
                raise PrizeAlreadyExistException()
            
    def get_one_by_id(self, id: int):
        with get_db() as session:
            db_object = session.query(Prize).filter_by(id=id).first()
            if not db_object:
                raise PrizeNotFoundException()
            return db_object
            
    def get_all(self, pagination: dict):
        limit = pagination.get('limit')
        offset = pagination.get('offset')
        with get_db() as session:
            db_object = session.query(Prize).limit(limit).offset(offset).all()
            return db_object
    
    def update_one(self, id: int, data: dict):
        with get_db() as session:
            try:
                db_object = session.query(Prize).filter_by(id=id).first()
                if not db_object:
                    raise PrizeNotFoundException()
                for key, value in data.items():
                    setattr(db_object, key, value)
                session.commit()
            except IntegrityError:
                raise PrizeAlreadyExistException()
            session.refresh(db_object)
            return db_object
    
    def delete_one(self, id: int):
        with get_db() as session:
            db_object = session.query(Prize).filter_by(id=id).first()
            if not db_object:
                raise PrizeNotFoundException()
            session.delete(db_object)
            session.commit()
        