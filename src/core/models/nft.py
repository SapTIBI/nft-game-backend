from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from src.core.models.association_tables import nft_user_table
from src.core.database import Base
from src.core.schemas.nft import NftSchema
class Nft(Base):
    __tablename__ = "nft"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    workBalance: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer, default=0)
    market_id: Mapped[int] = mapped_column(Integer, ForeignKey('market.id'))

    market: Mapped["Market"] = relationship("Market", back_populates="nfts")
    users: Mapped[list["User"]] = relationship("User", secondary=nft_user_table, back_populates="nfts")


    def to_read_model(self) -> NftSchema:
        return NftSchema(
            id=self.id,
            name=self.name,
            workBalance=self.workBalance,
            price=self.price,
            market_id=self.market_id
        )