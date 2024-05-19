from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.core.database import Base
from src.core.schemas.market import MarketSchema


class Market(Base):
    __tablename__ = "market"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)

    nfts: Mapped[list["Nft"]] = relationship("Nft", back_populates="market", cascade="all, delete-orphan")

    def to_read_model(self) -> MarketSchema:
        return MarketSchema(
            id=self.id,
            name=self.name,
        )