from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from src.core.exceptions import PrizeNotFoundException, PrizeAlreadyExistException
from src.core.schemas.prize import PrizeCreateSchema, PrizeUpdateSchema, PrizeSchema
from src.core.schemas.params import Paginator
from src.services.prize_service import PrizeService
router = APIRouter(
   prefix="/prizes",
   tags=["Prize"],
)

@router.post("/", status_code=201)
def create_prize(
   prize: PrizeCreateSchema,
   prizes_service:  Annotated[PrizeService, Depends(PrizeService)]):
   try:
      prize_id = prizes_service.create_prize(prize)
   except PrizeAlreadyExistException:
      raise HTTPException(status_code=403, detail="This prize already exist")
   except Exception:
      raise HTTPException(status_code=500, detail='Server error, unhandle')
   return {'prize_id': prize_id}

@router.get("/", status_code=200, response_model=List[PrizeSchema])
def get_prizes(
   prizes_service:  Annotated[PrizeService, Depends(PrizeService)],
   pagination: Paginator = Depends()
):
   prizes = prizes_service.get_prizes(pagination)
   return prizes

@router.put("/{prize_id}/", status_code=201, response_model=PrizeSchema)
def update_current_prize(
   prize_id: int,
   data: PrizeUpdateSchema,
   prizes_service:  Annotated[PrizeService, Depends(PrizeService)]):
   try:
      updated_prize = prizes_service.update_prize(prize_id, data)
   except PrizeNotFoundException:
      raise HTTPException(status_code=404, detail="This prize was not found")
   except PrizeAlreadyExistException:
      raise HTTPException(status_code=403, detail="This prize already exist")
   except Exception as e:
      raise HTTPException(status_code=500, detail='Server error, unhandle')
   return updated_prize

@router.get("/{prize_id}/", status_code=200, response_model=PrizeSchema)
def get_current_prize(
   prize_id: int,
   prizes_service:  Annotated[PrizeService, Depends(PrizeService)]):
   try:
      prize = prizes_service.get_prize(prize_id)
   except PrizeNotFoundException:
      raise HTTPException(status_code=404, detail="This prize was not found")
   except Exception:
      raise HTTPException(status_code=500, detail='Server error, unhandle')
   return prize

@router.delete("/{prize_id}/", status_code=204)
def delete_current_prize(
   prize_id: int,
   prizes_service:  Annotated[PrizeService, Depends(PrizeService)]):
   try:
      prizes_service.delete_prize(prize_id)
   except PrizeNotFoundException:
      raise HTTPException(status_code=404, detail="This prize was not found")
   except Exception as e:
      raise HTTPException(status_code=500, detail='Server error, unhandle')