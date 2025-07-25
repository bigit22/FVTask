import uvicorn
from fastapi import FastAPI
from src.api import task_router
from src.core.config import settings

app = FastAPI()

app.include_router(task_router)

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='127.0.0.1',
        port=80,
        reload=settings.DEBUG
    )
