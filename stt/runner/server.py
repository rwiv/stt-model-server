import uvicorn
from fastapi import FastAPI

from stt.env.env import get_env
from stt.routers import main, trans


def run():
    app = FastAPI()

    app.include_router(main.router)
    app.include_router(trans.router)

    env = get_env()
    uvicorn.run(app, port=env.port, host=env.host)
