from sqlalchemy.orm import Session

from src import schemas, exceptions
from src.db import models
#создаем в таблице Prize новую запись
def create_prize(db: Session, prize: schemas.PrizeCreateDTO):
    '''создаем в таблице Prize новую запись'''
    db_prize = models.Prize(value=prize.value)
    db.add(db_prize)
    db.commit()
    db.refresh(db_prize)
    return db_prize

#получаем из таблицы Prize запись
def get_prize(db: Session, prize_id: int):
    db_prize = db.query(models.Prize).filter(models.Prize.id == prize_id).first()
    if not db_prize:
        raise exceptions.PrizeNotFoundException()
    return db.query(models.Prize).filter(models.Prize.id == prize_id).first()

#обновляем запись в таблице Prize
def update_prize(db: Session, prize_id: int, updated_prize: schemas.PrizeUpdateDTO):
    db_prize = db.query(models.Prize).filter(models.Prize.id == prize_id).first()
    if not db_prize:
        raise exceptions.PrizeNotFoundException()
    for var, value in vars(updated_prize).items():
        setattr(db_prize, var, value) if value else None
        db.add(db_prize)
    db.commit()
    db.refresh(db_prize)
    return db_prize

#удаляем запись из таблицы Prize
def delete_prize(db: Session, prize_id: int):
    db_prize = db.query(models.Prize).filter(models.Prize.id == prize_id).first()
    if not db_prize:
        raise exceptions.PrizeNotFoundException()
    db.delete(db_prize)
    db.commit()
    
#добавляем пользователю приз, создается запись в таблице PrizeUser
def create_prize_user(db: Session, user_id: int, prize_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise exceptions.UserNotFoundException()
    db_prize = db.query(models.Prize).filter(models.Prize.id == prize_id).first()
    if not db_prize:
        raise exceptions.PrizeNotFoundException()
    db_user.prizes.append(db_prize)
    db.commit()


#получаем призы пользователя
def get_prizes_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise exceptions.UserNotFoundException()
    if not db_user.prizes:
        raise exceptions.PrizesUserNotFoundException()
    return db_user.prizes


#удаляем у пользователя приз, удаляется запись из таблицы PrizeUser
def delete_prize_user(db: Session, user_id: int, prize_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise exceptions.UserNotFoundException()
    db_prize = db.query(models.Prize).filter(models.Prize.id == prize_id).first()
    if not db_prize:
        raise exceptions.PrizeNotFoundException()
    db_user.prizes.remove(db_prize)
    db.commit()


#добавляем пользователю nft, создается запись в таблице NftUser
def create_nft_user(db: Session, user_id: int, nft_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise exceptions.UserNotFoundException()
    db_nft = db.query(models.Nft).filter(models.Nft.id == nft_id).first()
    if not db_nft:
        raise exceptions.NftNotFoundException()
    db_user.nfts.append(db_nft)
    db.commit()


#получаем nfts пользователя
def get_nfts_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise exceptions.UserNotFoundException()
    if not db_user.nfts:
        raise exceptions.NftsUserNotFoundException()
    return db_user.nfts


#удаляем у пользователя nft, удаляется запись из таблицы NftUser
def delete_nft_user(db: Session, user_id: int, nft_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise exceptions.UserNotFoundException()
    db_nft = db.query(models.Nft).filter(models.Nft.id == nft_id).first()
    if not db_nft:
        raise exceptions.NftNotFoundException()
    if db_nft not in db_user.nfts:
        raise exceptions.NftUserNotFoundException()
    db_user.nfts.remove(db_nft)
    db.commit()




#получаем из таблицы User запись
def get_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise exceptions.UserNotFoundException()
    return db_user

#получаем из таблицы User запись
def get_user_by_email(db: Session, email: str):
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if not db_user:
        raise exceptions.UserNotFoundException()
    return db_user


#получаем из таблицы User запись
def get_user_by_username(db: Session, username: str):
    db_user = db.query(models.User).filter(models.User.username == username).first()
    if not db_user:
        raise exceptions.UserNotFoundException()
    return db_user

#получаем из таблицы User записи
def get_users(db: Session, skip: int = 0, limit: int = 100):
    db_users = db.query(models.User).offset(skip).limit(limit).all()
    if not db_users:
        raise exceptions.UserNotFoundException()
    return db_users

#создаем запись в таблице User
def create_user(db: Session, user: schemas.UserCreateDTO):
    db_user = db.query(models.User).filter((models.User.email == user.email) | (models.User.tgToken == user.tgToken)).first()
    if db_user:
        raise exceptions.UserAlreadyExistException()
    db_user = models.User(
        username=user.username,
        tgToken=user.tgToken,
        email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#удаляем запись из таблицы User
def delete_user(db: Session,  user_id):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise exceptions.UserNotFoundException()
    db.delete(db_user)
    db.commit()

#обновляем запись в таблице User    
def update_user(db: Session, user_id: int, updated_user: schemas.UserUpdateDTO):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise exceptions.UserNotFoundException()
    for var, value in vars(updated_user).items():
        print(var, value)
        setattr(db_user, var, value) if value else None
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#создаем запись в таблице Nft
def create_nft(db: Session, nft: schemas.NftCreateDTO):
    db_market = db.query(models.Market).filter(models.Market.id == nft.market_id).first()
    if not db_market:
        raise exceptions.MarketNotFoundException()
    db_nft = db.query(models.Nft).filter(models.Nft.name == nft.name, models.Nft.market_id == nft.market_id ).first()
    if db_nft:
        raise exceptions.NftAlreadyExistException()
    db_nft = models.Nft(
        market_id=nft.market_id,
        name=nft.name,
        workBalance=nft.workBalance,
        price=nft.price
    )
    db.add(db_nft)
    db.commit()
    db.refresh(db_nft)
    return db_nft


#обновляем запись в таблице Nft
def update_nft(db: Session, nft_id: int, updated_nft: schemas.NftUpdateDTO):
    db_nft = db.query(models.Nft).filter(models.Nft.id == nft_id).first()
    if not db_nft:
        raise exceptions.NftNotFoundException()
    for var, value in vars(updated_nft).items():
        setattr(db_nft, var, value) if value else None
    db.add(db_nft)
    db.commit()
    db.refresh(db_nft)
    return db_nft


#создаем запись в таблице Nft
def get_nft(db: Session, nft_id: int):
    db_nft = db.query(models.Nft).filter(models.Nft.id == nft_id).first()
    if not db_nft:
        raise exceptions.NftNotFoundException()
    return db_nft


#удаляем запись из таблицы Nft
def delete_nft(db: Session, nft_id: int):
    db_nft = db.query(models.Nft).filter(models.Nft.id == nft_id).first()
    if not db_nft:
        raise exceptions.NftNotFoundException()
    db.delete(db_nft)
    db.commit()
    
#создаем запись в таблице Market
def create_market(db: Session, market: schemas.MarketCreateDTO):
    db_market = db.query(models.Market).filter(models.Market.name == market.name).first()
    if db_market:
        raise exceptions.MarketAlreadyExistException()
    db_market = models.Market(
        name=market.name
    )
    db.add(db_market)
    db.commit()
    db.refresh(db_market)
    return db_market


#получаем запись в таблице Market
def get_market(db: Session, market_id: int):
    db_market = db.query(models.Market).filter(models.Market.id == market_id).first()
    if not db_market:
        raise exceptions.MarketNotFoundException()
    return db_market   


#обновляем запись в таблице Market
def update_market(db: Session, market_id: int, updated_market: schemas.MarketUpdateDTO):
    db_market = db.query(models.Market).filter(models.Market.id == market_id).first()
    if not db_market:
        raise exceptions.MarketNotFoundException()
    for var, value in vars(updated_market).items():
        setattr(db_market, var, value) if value else None
    db.add(db_market)
    db.commit()
    db.refresh(db_market)
    return db_market


#удаляем запись в таблице Market
def delete_market(db: Session,  market_id: int):
    db_market = db.query(models.Market).filter(models.Market.id == market_id).first()
    if not db_market:
        raise exceptions.MarketNotFoundException()
    db.delete(db_market)
    db.commit()