from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from src.core.exceptions import MarketNotFoundException, MarketAlreadyExistException
from src.core.schemas.market import MarketCreateSchema, MarketUpdateSchema, MarketSchema
from src.core.schemas.nft import NftSchema
from src.core.schemas.params import Paginator
from src.services.market_service import MarketService
from src.api.dependencies import markets_service


router = APIRouter(
   prefix="/markets",
   tags=["Market"],
)


@router.post("/", status_code=201)
def create_market(
   market: MarketCreateSchema,
   markets_service:  Annotated[MarketService, Depends(markets_service)]):
   try:
      market_id = markets_service.create_market(market)
   except MarketAlreadyExistException:
      raise HTTPException(status_code=403, detail="This market already exist")
   except Exception:
      raise HTTPException(status_code=500, detail='Server error, unhandle')
   return {'market_id': market_id}

@router.get("/", status_code=200, response_model=List[MarketSchema])
def get_markets(
   markets_service:  Annotated[MarketService, Depends(markets_service)],
   pagination: Paginator = Depends()
):
   markets = markets_service.get_markets(pagination)
   return markets

@router.put("/{market_id}/", status_code=201, response_model=MarketSchema)
def update_current_market(
   market_id: int,
   data: MarketUpdateSchema,
   markets_service:  Annotated[MarketService, Depends(markets_service)]):
   try:
      updated_market = markets_service.update_market(market_id, data)
   except MarketNotFoundException:
      raise HTTPException(status_code=404, detail="This market was not found")
   except MarketAlreadyExistException:
      raise HTTPException(status_code=403, detail="This market already exist")
   except Exception as e:
      print(e)
      raise HTTPException(status_code=500, detail='Server error, unhandle')
   return updated_market

@router.get("/{market_id}/", status_code=200, response_model=MarketSchema)
def get_current_market(
   market_id: int,
   markets_service:  Annotated[MarketService, Depends(markets_service)]):
   try:
      market = markets_service.get_market(market_id)
   except MarketNotFoundException:
      raise HTTPException(status_code=404, detail="This market was not found")
   except Exception:
      raise HTTPException(status_code=500, detail='Server error, unhandle')
   return market

@router.delete("/{market_id}/", status_code=204)
def delete_current_market(
   market_id: int,
   markets_service:  Annotated[MarketService, Depends(markets_service)]):
   try:
      markets_service.delete_market(market_id)
   except MarketNotFoundException:
      raise HTTPException(status_code=404, detail="This market was not found")
   except Exception as e:
      raise HTTPException(status_code=500, detail='Server error, unhandle')
   
@router.get("/{market_id}/nfts/", status_code=200, response_model=List[NftSchema])
def get_nfts_for_current_market(
    market_id: int, 
    markets_service:  Annotated[MarketService, Depends(markets_service)]):
    try:
        nfts = markets_service.get_nfts_for_market(market_id)
    except MarketNotFoundException:
        raise HTTPException(status_code=404, detail="This market was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return nfts
