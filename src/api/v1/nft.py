from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from src.core.exceptions import NftNotFoundException, NftAlreadyExistException, MarketNotFoundException
from src.core.schemas.nft import NftCreateSchema, NftUpdateSchema, NftSchema
from src.core.schemas.params import Paginator
from src.services.nft_service import NftService
router = APIRouter(
   prefix="/nfts",
   tags=["NFT"],
)

@router.post("/", status_code=201)
def create_nft(
   nft: NftCreateSchema,
   nfts_service:  Annotated[NftService, Depends(NftService)]):
   try:
      nft_id = nfts_service.create_nft(nft)
   except NftAlreadyExistException:
      raise HTTPException(status_code=403, detail="This nft already exist")
   except MarketNotFoundException:
      raise HTTPException(status_code=404, detail="This market was not found")
   except Exception:
      raise HTTPException(status_code=500, detail='Server error, unhandle')
   return {'nft_id': nft_id}

@router.get("/", status_code=200, response_model=List[NftSchema])
def get_nfts(
   nfts_service:  Annotated[NftService, Depends(NftService)],
   pagination: Paginator = Depends()
):
   nfts = nfts_service.get_nfts(pagination)
   return nfts

@router.put("/{nft_id}/", status_code=201, response_model=NftSchema)
def update_current_nft(
   nft_id: int,
   data: NftUpdateSchema,
   nfts_service:  Annotated[NftService, Depends(NftService)]):
   try:
      updated_nft = nfts_service.update_nft(nft_id, data)
   except NftNotFoundException:
      raise HTTPException(status_code=404, detail="This nft was not found")
   except NftAlreadyExistException:
      raise HTTPException(status_code=403, detail="This nft already exist")
   except Exception as e:
      raise HTTPException(status_code=500, detail='Server error, unhandle')
   return updated_nft

@router.get("/{nft_id}/", status_code=200, response_model=NftSchema)
def get_current_nft(
   nft_id: int,
   nfts_service:  Annotated[NftService, Depends(NftService)]):
   try:
      nft = nfts_service.get_nft(nft_id)
   except NftNotFoundException:
      raise HTTPException(status_code=404, detail="This nft was not found")
   except Exception:
      raise HTTPException(status_code=500, detail='Server error, unhandle')
   return nft

@router.delete("/{nft_id}/", status_code=204)
def delete_current_nft(
   nft_id: int,
   nfts_service:  Annotated[NftService, Depends(NftService)]):
   try:
      nfts_service.delete_nft(nft_id)
   except NftNotFoundException:
      raise HTTPException(status_code=404, detail="This nft was not found")
   except Exception as e:
      raise HTTPException(status_code=500, detail='Server error, unhandle')