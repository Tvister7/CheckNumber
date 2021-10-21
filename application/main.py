import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from database import init_db
from endpoints import stop_list

app = FastAPI(title="StopList")


@app.on_event("startup")
async def startup_event():
    init_db(app)

app.include_router(stop_list.router, prefix="/api/phones", tags=["phone"])

load_dotenv("../.env")
HOST = os.environ["UVICORN_HOST"]
PORT = int(os.environ["UVICORN_PORT"])


if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, host=HOST, reload=True)
