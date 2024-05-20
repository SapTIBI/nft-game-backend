from src.core.schemas.nft import NftCreateSchema, NftUpdateSchema
from src.core.schemas.params import Paginator
from src.repositories.nft import NftRepository


class NftService:

    def __init__(
        self,
        nft_repo: NftRepository):
        self.nft_repo: NftRepository = nft_repo()

    def create_nft(self, nft: NftCreateSchema):
        nft_dict = nft.model_dump()
        nft_id = self.nft_repo.create_one(nft_dict)
        return nft_id

    def get_nft(self, id: int):
        nft = self.nft_repo.get_one_by_id(id)
        return nft.to_read_model()

    def get_nfts(self, pagination: Paginator):
        pagination_dict = pagination.model_dump()
        nfts = self.nft_repo.get_all(pagination_dict)
        return nfts

    def update_nft(self, nft_id: int, data: NftUpdateSchema):
        update_nft_dict = data.model_dump()
        updated_nft = self.nft_repo.update_one(nft_id, update_nft_dict)
        return updated_nft.to_read_model()

    def delete_nft(self, nft_id: int):
        self.nft_repo.delete_one(nft_id)