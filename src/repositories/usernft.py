from src.core.database import get_db
from src.core.models.user import User
from src.core.models.nft import Nft
from src.core.exceptions import UserNotFoundException, NftNotFoundException

class UserNftRepository:
    def add_nft_for_user(self, user_id: int, nft_id: int):
        with get_db() as session:
            db_user = session.query(User).filter(User.id == user_id).first()
            if not db_user:
                raise UserNotFoundException()
            db_nft = session.query(Nft).filter(Nft.id == nft_id).first()
            if not db_nft:
                raise NftNotFoundException()
            db_user.nfts.append(db_nft)
            session.commit()

    def get_nfts_for_user(self, user_id: int):
        with get_db() as session:
            db_user = session.query(User).filter(User.id == user_id).first()
            if not db_user:
                raise UserNotFoundException()
            return db_user.nfts

    def delete_nft_for_user(self, user_id: int, nft_id: int):
        with get_db() as session:
            db_user = session.query(User).filter(User.id == user_id).first()
            if not db_user:
                raise UserNotFoundException()
            db_nft = session.query(Nft).filter(Nft.id == nft_id).first()
            if not db_nft:
                raise NftNotFoundException()
            db_user.nfts.remove(db_nft)
            session.commit()