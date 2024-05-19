from typing import Optional, List, Annotated
from src.core.schemas.user import UserCreateSchema, UserUpdateSchema
from src.core.schemas.params import Paginator
from src.repositories.user import UserRepository
from src.repositories.userprize import UserPrizeRepository
from src.repositories.usernft import UserNftRepository


class UserService:

    def __init__(self):
        self.user_repo = UserRepository()
        self.userprize_repo = UserPrizeRepository()
        self.usernft_repo = UserNftRepository()

    def create_user(self, data: UserCreateSchema):
        user_dict = data.model_dump()
        user_id = self.user_repo.create_one(user_dict)
        return user_id

    def get_user(self, id: int):
        user = self.user_repo.get_one_by_id(id)
        return user.to_read_model()

    def get_users(self, pagination: Paginator):
        pagination_dict = pagination.model_dump()
        users = self.user_repo.get_all(pagination_dict)
        return users
    
    def update_user(self, user_id: int, data: UserUpdateSchema):
        update_user_dict = data.model_dump()
        updated_user = self.user_repo.update_one(user_id, update_user_dict)
        return updated_user.to_read_model()

    def delete_user(self, user_id: int):
        self.user_repo.delete_one(user_id)

    def add_prize_for_user(self, user_id: int, prize_id: int):
        self.userprize_repo.add_prize_for_user(user_id, prize_id)

    def get_prizes_for_user(self, user_id: int):
        return self.userprize_repo.get_prizes_for_user(user_id)
    
    def delete_prize_for_user(self, user_id: int, prize_id: int):
        self.userprize_repo.delete_prize_for_user(user_id, prize_id)
    
    def add_nft_for_user(self, user_id: int, nft_id: int):
        self.usernft_repo.add_nft_for_user(user_id, nft_id)

    def get_nfts_for_user(self, user_id: int):
        return self.usernft_repo.get_nfts_for_user(user_id)
    
    def delete_nft_for_user(self, user_id: int, nft_id: int):
        self.usernft_repo.delete_nft_for_user(user_id, nft_id)