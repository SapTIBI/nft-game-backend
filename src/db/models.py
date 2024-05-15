from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.db.database import Base


class Prize(Base):
    __tablename__ = "prize"


    id = Column(Integer, primary_key=True)
    value = Column(String)
    users = relationship("User", secondary='prizeuser', back_populates="prizes")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    tgToken = Column(String, unique=True, index=True)
    balance = Column(Integer, default=0)
    role = Column(String, default='base_role')
    refScore = Column(Integer, default=0)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=func.now())

    prizes = relationship("Prize", secondary='prizeuser', back_populates="users")
    nfts = relationship("Nft", secondary='nftuser', back_populates="users")

class PrizeUser(Base):
    __tablename__ = "prizeuser"

    id = Column(Integer, primary_key=True)  
    prize_id = Column(Integer, ForeignKey('prize.id', ondelete='CASCADE'))
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))




class Nft(Base):
    __tablename__ = "nft"


    id = Column(Integer, primary_key=True)
    name = Column(String)
    workBalance = Column(String)
    price = Column(Integer, default=0)
    market_id = Column(Integer, ForeignKey('market.id'))

    market = relationship("Market", back_populates="nfts")
    users = relationship("User", secondary='nftuser', back_populates="nfts")

class NftUser(Base):
    __tablename__ = "nftuser"

    id = Column(Integer, primary_key=True)  
    nft_id = Column(Integer, ForeignKey('nft.id', ondelete='CASCADE'))
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))

class Market(Base):
    __tablename__ = "market"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)

    nfts = relationship("Nft", back_populates="market")