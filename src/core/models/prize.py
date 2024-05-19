from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.core.database import Base
from src.core.schemas.prize import PrizeSchema


class Prize(Base):
    __tablename__ = "prize"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    value: Mapped[str] = mapped_column(String)
    users: Mapped[list["User"]] = relationship("User", secondary='prizeuser', back_populates="prizes")
    
    def to_read_model(self) -> PrizeSchema:
        return PrizeSchema(
            id=self.id,
            value=self.value,
        )