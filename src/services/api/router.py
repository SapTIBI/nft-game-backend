from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src import schemas, exceptions
from src.db import crud, database
router = APIRouter(
   prefix="/api/v1",
   tags=["Таски"],
)

@router.post("/prizes/",  status_code=201)
def create_prize(prize_data: schemas.PrizeCreateDTO , db: Session = Depends(database.get_db)):
    return crud.create_prize(db, prize_data)

@router.get("/prizes/", status_code=200)
def get_prize(prize_id: int, db: Session = Depends(database.get_db)):
    try: 
        prize = crud.get_prize(db, prize_id)
    except exceptions.PrizeNotFoundException:
        raise HTTPException(status_code=404, detail="This prize was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return prize

@router.put("/prizes/", status_code=201)
def update_prize(prize_id: int, prize_data: schemas.PrizeUpdateDTO, db: Session = Depends(database.get_db)):
    try: 
        updated_prize = crud.update_prize(db, prize_id, prize_data)
    except exceptions.PrizeNotFoundException:
        raise HTTPException(status_code=404, detail="This prize was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return updated_prize

@router.delete("/prizes/", status_code=204)
def delete_prize(prize_id: int, db: Session = Depends(database.get_db)):
    try: 
        crud.delete_prize(db, prize_id)
    except exceptions.PrizeNotFoundException:
        raise HTTPException(status_code=404, detail="This prize was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')

@router.post("/users/", status_code=201)
def create_user(user_data: schemas.UserCreateDTO, db: Session = Depends(database.get_db)):
    try:
        created_user = crud.create_user(db=db, user=user_data)
    except exceptions.UserAlreadyExistException:
        raise HTTPException(status_code=403, detail="This user already exist")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return created_user

@router.get("/users/", status_code=200)
def get_users(user_id: int, db: Session = Depends(database.get_db)):
    try:
        user = crud.get_user(db, user_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return user

@router.put("/users/", status_code=201)
def update_user(user_id: int, user_data: schemas.UserUpdateDTO, db: Session = Depends(database.get_db)):
    try:
        updated_user = crud.update_user(db, user_id, user_data)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return updated_user
    

@router.delete("/users/", status_code=204)
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    try:
        crud.delete_user(db, user_id)
    except exceptions.PrizeNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')


@router.post("/users/prizes/", status_code=204)
def add_user_prize(user_prize_data: schemas.UserPrizeCreateDTO, db: Session = Depends(database.get_db)):
    try:
        crud.create_prize_user(db, user_prize_data.user_id,  user_prize_data.prize_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except exceptions.PrizeNotFoundException:
        raise HTTPException(status_code=404, detail="This prize was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')

@router.get('/users/prizes/', status_code=200)
def get_user_prizes(user_id: int, db: Session = Depends(database.get_db)):
    try:
        prizes_user = crud.get_prizes_user(db, user_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except exceptions.PrizesUserNotFoundException:
        raise HTTPException(status_code=404, detail="There are no prizes for this user")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return prizes_user
    
@router.delete("/users/prizes/", status_code=204)
def delete_user_prize(user_prize_data: schemas.UserPrizeDeleteDTO, db: Session = Depends(database.get_db)):
    try:
        crud.delete_prize_user(db, user_prize_data.user_id,  user_prize_data.prize_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except exceptions.PrizeNotFoundException:
        raise HTTPException(status_code=404, detail="This prize was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
#----

@router.post("/users/nfts/", status_code=204)
def add_user_nft(user_nft_data: schemas.UserNftCreateDTO, db: Session = Depends(database.get_db)):
    try:
        crud.create_nft_user(db, user_nft_data.user_id,  user_nft_data.nft_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except exceptions.NftNotFoundException:
        raise HTTPException(status_code=404, detail="This nft was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')

@router.get('/users/nfts/', status_code=200)
def get_user_prizes(user_id: int, db: Session = Depends(database.get_db)):
    try:
        nfts_user = crud.get_nfts_user(db, user_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except exceptions.NftsUserNotFoundException:
        raise HTTPException(status_code=404, detail="There are no nfts for this user")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return nfts_user

@router.delete("/users/nfts/", status_code=204)
def delete_user_prize(user_nft_data: schemas.UserNftDeleteDTO, db: Session = Depends(database.get_db)):
    try:
        crud.delete_nft_user(db, user_nft_data.user_id,  user_nft_data.nft_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except exceptions.NftNotFoundException:
        raise HTTPException(status_code=404, detail="This nft was not found")
    except exceptions.NftUserNotFoundException:
        raise HTTPException(status_code=404, detail="There is no this NFT for this user")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')


#----
@router.post("/nfts/", status_code=201)
def create_nft(nft_data: schemas.NftCreateDTO, db: Session = Depends(database.get_db)):
    try:
        created_nft = crud.create_nft(db, nft_data)
    except exceptions.NftAlreadyExistException:
        raise HTTPException(status_code=403, detail="This nft already exists")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return created_nft

@router.get("/nfts/", status_code=200)
def get_nft(nft_id: int, db: Session = Depends(database.get_db)):
    try:
        nft = crud.get_nft(db, nft_id)
    except exceptions.NftNotFoundException:
        raise HTTPException(status_code=404, detail="This nft was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return nft

@router.put("/nfts/", status_code=201)
def update_market(nft_id: int, nft_data: schemas.NftUpdateDTO, db: Session = Depends(database.get_db)):
    try:
        updated_nft = crud.update_nft(db, nft_id, nft_data)
    except exceptions.NftNotFoundException:
        raise HTTPException(status_code=404, detail="This nft was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return updated_nft


@router.delete("/nfts/", status_code=204)
def delete_market(nft_id: int, db: Session = Depends(database.get_db)):
    try:
        crud.delete_nft(db, nft_id)
    except exceptions.NftNotFoundException:
        raise HTTPException(status_code=404, detail="This nft was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')

@router.post("/markets/", status_code=201)
def create_market(market_data: schemas.MarketCreateDTO, db: Session = Depends(database.get_db)):
    try:
        created_market = crud.create_market(db, market_data)
    except exceptions.MarketAlreadyExistException:
        raise HTTPException(status_code=403, detail="This market already exists")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return created_market

@router.get("/markets/", status_code=200)
def get_market(market_id: int, db: Session = Depends(database.get_db)):
    try:
        market = crud.get_market(db, market_id)
    except exceptions.MarketNotFoundException:
        raise HTTPException(status_code=404, detail="This market was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return market

@router.put("/markets/", status_code=201)
def update_market(market_id: int, market_data: schemas.MarketUpdateDTO, db: Session = Depends(database.get_db)):
    try:
        updated_market = crud.update_market(db, market_id, market_data)
    except exceptions.MarketNotFoundException:
        raise HTTPException(status_code=404, detail="This market was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return updated_market


@router.delete("/markets/", status_code=204)
def delete_market(market_id: int, db: Session = Depends(database.get_db)):
    try:
        crud.delete_market(db, market_id)
    except exceptions.MarketNotFoundException:
        raise HTTPException(status_code=404, detail="This market was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')