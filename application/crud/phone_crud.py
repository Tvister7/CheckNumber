from application.models.phone_model import Phone


async def get_phone(phone: str) -> Phone | None:
    try:
        phone_number = await Phone.get(phone=phone)
        if not phone_number:
            return None
        return phone_number
    except:
        return None


async def create_phone(phone: str) -> None:
    await Phone.create(phone=phone)
