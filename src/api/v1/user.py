from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from src.core import exceptions
from src.core.schemas.user import UserCreateSchema, UserUpdateSchema, UserSchema
from src.core.schemas.prize import PrizeSchema
from src.core.schemas.nft import NftSchema
from src.core.schemas.params import Paginator
from src.services.user_service import UserService

router = APIRouter(
   prefix="/users",
   tags=["User"],
)

@router.post("/", status_code=201)#UserSchema
def create_user(
    user: UserCreateSchema,
    users_service:  Annotated[UserService, Depends(UserService)]):
    try:
        user_id = users_service.create_user(user)
    except exceptions.UserAlreadyExistException:
        raise HTTPException(status_code=403, detail="This user already exist")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return {'user_id': user_id}

@router.get("/", status_code=200, response_model=List[UserSchema])
def get_users(
    users_service:  Annotated[UserService, Depends(UserService)],
    pagination: Paginator = Depends()
):
    users = users_service.get_users(pagination)
    return users

@router.put("/{user_id}/", status_code=201, response_model=UserSchema)
def update_current_user(
    user_id: int,
    data: UserUpdateSchema,
    users_service:  Annotated[UserService, Depends(UserService)]):
    try:
        updated_user = users_service.update_user(user_id, data)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except exceptions.UserAlreadyExistException:
        raise HTTPException(status_code=403, detail="This user already exist")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return updated_user

@router.get("/{user_id}/", status_code=200, response_model=UserSchema)
def get_current_user(
    user_id: int,
    users_service:  Annotated[UserService, Depends(UserService)]):
    try:
        user = users_service.get_user(user_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return user

@router.delete("/{user_id}/", status_code=204)
def delete_current_user(
    user_id: int,
    users_service:  Annotated[UserService, Depends(UserService)]):
    try:
        user = users_service.delete_user(user_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')

@router.post("/{user_id}/nfts/", status_code=204)
def add_nft_for_current_user(
    user_id: int, 
    nft_id: int,
    users_service:  Annotated[UserService, Depends(UserService)]):
    try:
        users_service.add_nft_for_user(user_id, nft_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except exceptions.NftNotFoundException:
        raise HTTPException(status_code=404, detail="This nft was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')

@router.get("/{user_id}/nfts/", status_code=200, response_model=List[NftSchema])
def get_nfts_for_current_user(
    user_id: int, 
    users_service:  Annotated[UserService, Depends(UserService)]):
    try:
        nfts = users_service.get_nfts_for_user(user_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return nfts

@router.delete("/{user_id}/nfts/", status_code=204)
def delete_current_nft_for_current_user(
    user_id: int, 
    nft_id: int,
    users_service:  Annotated[UserService, Depends(UserService)]):
    try:
        users_service.delete_nft_for_user(user_id, nft_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except exceptions.NftNotFoundException:
        raise HTTPException(status_code=404, detail="This nft was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')

@router.post("/{user_id}/prizes/", status_code=204)
def add_prize_for_current_user(
    user_id: int, 
    prize_id: int,
    users_service:  Annotated[UserService, Depends(UserService)]):
    try:
        users_service.add_prize_for_user(user_id, prize_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except exceptions.PrizeNotFoundException:
        raise HTTPException(status_code=404, detail="This prize was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')

@router.get("/{user_id}/prizes/", status_code=200, response_model=List[PrizeSchema])
def get_prizes_for_current_user(
    user_id: int, 
    users_service:  Annotated[UserService, Depends(UserService)]):
    try:
        prizes = users_service.get_prizes_for_user(user_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')
    return prizes

@router.delete("/{user_id}/prizes/", status_code=204)
def delete_current_prize_for_current_user(
    user_id: int, 
    prize_id: int,
    users_service:  Annotated[UserService, Depends(UserService)]):
    try:
        users_service.delete_prize_for_user(user_id, prize_id)
    except exceptions.UserNotFoundException:
        raise HTTPException(status_code=404, detail="This user was not found")
    except exceptions.PrizeNotFoundException:
        raise HTTPException(status_code=404, detail="This prize was not found")
    except Exception:
        raise HTTPException(status_code=500, detail='Server error, unhandle')