from fastapi import APIRouter
from application.utilities.phone_in_db import number_in_dbase

router = APIRouter()


@router.get("/test_number/{phone}")
async def test_number(phone: str):
    found = await number_in_dbase(phone)
    return {"found": found}

