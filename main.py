import uvicorn
from fastapi import FastAPI
from stt.routers import main, trans

app = FastAPI()

app.include_router(main.router)
app.include_router(trans.router)

if __name__ == "__main__":
    # uvicorn.run(app, port=8080, reload=True)
    uvicorn.run(app, port=8080)
