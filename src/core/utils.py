from src.core.database import Base, engine
from src.core.models.user import User
from src.core.models.prize import Prize
from src.core.models.nft import Nft
from src.core.models.market import Market


# создаем все таблицы определнные в моделях
def create_tables():
     Base.metadata.create_all(bind=engine)
