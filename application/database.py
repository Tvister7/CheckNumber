import os
from dotenv import load_dotenv
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

load_dotenv("../.env")
TORTOISE_DATABASE_URL = os.environ["DATABASE_URL"]


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=TORTOISE_DATABASE_URL,
        modules={"models": ["application.models.phone_model"]},
        generate_schemas=True,
        add_exception_handlers=True
    )
