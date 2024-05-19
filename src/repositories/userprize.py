from src.core.database import get_db
from src.core.models.user import User
from src.core.models.prize import Prize
from src.core.exceptions import UserNotFoundException, PrizeNotFoundException
from sqlalchemy.exc import IntegrityError

class UserPrizeRepository:
    def add_prize_for_user(self, user_id: int, prize_id: int):
        with get_db() as session:
            db_user = session.query(User).filter(User.id == user_id).first()
            if not db_user:
                raise UserNotFoundException()
            db_prize = session.query(Prize).filter(Prize.id == prize_id).first()
            if not db_prize:
                raise PrizeNotFoundException()
            db_user.prizes.append(db_prize)
            session.commit()

    def get_prizes_for_user(self, user_id: int):
        with get_db() as session:
            db_user = session.query(User).filter(User.id == user_id).first()
            if not db_user:
                raise UserNotFoundException()
            return db_user.prizes

    def delete_prize_for_user(self, user_id: int, prize_id: int):
        with get_db() as session:
            db_user = session.query(User).filter(User.id == user_id).first()
            if not db_user:
                raise UserNotFoundException()
            db_prize = session.query(Prize).filter(Prize.id == prize_id).first()
            if not db_prize:
                raise PrizeNotFoundException()
            db_user.prizes.remove(db_prize)
            session.commit()