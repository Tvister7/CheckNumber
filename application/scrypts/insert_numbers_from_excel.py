import asyncio
import csv
import os
import asyncpg
from dotenv import load_dotenv
from application.utilities.phone_in_db import test_phone


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILE_NAME = input("Введите название csv-файла для загрузки номеров в базу:")
# FILE_NAME = "phones.csv"
load_dotenv(os.path.join(BASE_DIR, ".env"))
DATABASE_USER = os.environ["DATABASE_USER"]
DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
DATABASE_HOST = os.environ["DATABASE_HOST"]
DATABASE_NAME = os.environ["DATABASE_NAME"]
STATEMENT = "INSERT INTO phone (phone) VALUES ($1)"


async def insert_phones():
    conn = await asyncpg.connect(user=DATABASE_USER, password=DATABASE_PASSWORD,
                                 database=DATABASE_NAME, host=DATABASE_HOST)
    data = []

    with open(os.path.join(BASE_DIR, FILE_NAME), encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file)
        number_of_phones = 0
        number_of_wrong_phones = 0
        for row in file_reader:
            phone = row[0]
            if test_phone(phone):
                data.append((phone, ))
                number_of_phones += 1
            else:
                number_of_wrong_phones += 1

        await conn.executemany(STATEMENT, data)

        print(f"Записано {number_of_phones} номеров")
        print(f"{number_of_wrong_phones} ошибочных номеров")

    await conn.close()


asyncio.run(insert_phones())
