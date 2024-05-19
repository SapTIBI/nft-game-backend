from src.core.schemas.prize import PrizeCreateSchema, PrizeUpdateSchema
from src.core.schemas.params import Paginator
from src.repositories.prize import PrizeRepository


class PrizeService:
    def __init__(self):
        self.prize_repo = PrizeRepository()

    def create_prize(self, prize: PrizeCreateSchema):
        prize_dict = prize.model_dump()
        prize_id = self.prize_repo.create_one(prize_dict)
        return prize_id

    def get_prize(self, id: int):
        prize = self.prize_repo.get_one_by_id(id)
        return prize.to_read_model()

    def get_prizes(self, pagination: Paginator):
        pagination_dict = pagination.model_dump()
        prizes = self.prize_repo.get_all(pagination_dict)
        return prizes

    def update_prize(self, prize_id: int, data: PrizeUpdateSchema):
        update_prize_dict = data.model_dump()
        updated_prize = self.prize_repo.update_one(prize_id, update_prize_dict)
        return updated_prize.to_read_model()

    def delete_prize(self, prize_id: int):
        self.prize_repo.delete_one(prize_id)