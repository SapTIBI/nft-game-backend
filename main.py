from fastapi import FastAPI

from src.services.api import api_router
app = FastAPI()
from src.db.database import engine
from src.db import models
models.Base.metadata.create_all(bind=engine)
app.include_router(api_router)