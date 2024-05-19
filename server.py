import uvicorn
from fastapi import FastAPI

from src.api import api_v1
from src.core.utils import create_tables
app = FastAPI()
app.include_router(api_v1)

if __name__ == "__main__":
    create_tables()
    uvicorn.run(
        'server:app',
        reload=True
    )