from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.core.database import Base
from src.core.schemas.user import UserSchema

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    tgToken: Mapped[str] = mapped_column(String, unique=True, index=True)
    balance: Mapped[int] = mapped_column(Integer, default=0)
    role: Mapped[str] = mapped_column(String, default='base_role')
    refScore: Mapped[int] = mapped_column(Integer, default=0)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    prizes: Mapped[list["Prize"]] = relationship("Prize", secondary='prizeuser', back_populates="users")
    nfts: Mapped[list["Nft"]] = relationship("Nft", secondary='nftuser', back_populates="users")

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            username=self.username,
            tgToken=self.tgToken,
            balance=self.balance,
            role=self.role,
            refScore=self.refScore,
            email=self.email,
            created_at=self.created_at
        )