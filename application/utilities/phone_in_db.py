import re
from fastapi import HTTPException
from application.crud.phone_crud import get_phone

phone_pattern = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'


def test_phone(phone: str) -> bool:
    if (len(phone) in range(11, 16)) and re.match(phone_pattern, phone):
        return True
    return False


async def number_in_dbase(phone: str) -> int:
    if not test_phone(phone):
        raise HTTPException(422, detail="Input string is not a phone number!")
    if not await get_phone(phone):
        return 0
    return 1
