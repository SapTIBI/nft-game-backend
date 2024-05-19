# NFTGame-backend

## Installation
```bash 
git clone https://github.com/SapTIBI/nft-game-backend.git
cd ./nft-game-backend
python -m venv venv
source venv/Scripts/activate
pip install -r ./requirements/dev.txt
python server.py
```

## Running an existing project
```bash
cd ./nft-game-backend
source venv/Scripts/activate
python server.py
```
После чего запустится локальный сервер адресу: *http://127.0.0.1:8000*  
Документация по API будет доступна по адресу: *http://127.0.0.1:8000/docs*

Параметры запуска для uvicorn можно посмотреть тут: https://www.uvicorn.org/
