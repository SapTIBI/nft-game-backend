from sqlalchemy import Table, Column, Integer, ForeignKey

from src.core.database import Base

prize_user_table = Table(
    'prizeuser',
    Base.metadata,
    Column('prize_id', Integer, ForeignKey('prize.id', ondelete='CASCADE')),
    Column('user_id', Integer, ForeignKey('user.id', ondelete='CASCADE'))
)

nft_user_table = Table(
    'nftuser',
    Base.metadata,
    Column('nft_id', Integer, ForeignKey('nft.id', ondelete='CASCADE')),
    Column('user_id', Integer, ForeignKey('user.id', ondelete='CASCADE'))
)