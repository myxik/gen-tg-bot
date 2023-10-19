import os
import time
import uuid
import asyncio
import logging
import psycopg2

from redis import Redis
from rq import Queue
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from const import INSERT, FIND, UPDATE, HELLO_STR
from generation import call_generation
load_dotenv()


conn = psycopg2.connect("postgresql://postgres:123@localhost/genbot")
cursor = conn.cursor()
logging.basicConfig(level=logging.INFO)
API_TOKEN = os.getenv("TELEGRAM_TOKEN")
redis_conn = Redis()
q = Queue(connection=redis_conn)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(HELLO_STR)


@dp.message(Command("add_prompt"))
async def add_prompt(message: types.Message):
    """
    Firstly, generate unique uuid associated with this generation, say it to user
    then, enter the related info to the database
    """
    unique_uuid = str(uuid.uuid4())
    await message.answer(f"Your generation id is {unique_uuid}")
    user_id = message.from_user.id
    chat_id = message.chat.id

    prompt = message.text.replace("/add_prompt ", "")

    cursor.execute(INSERT, (unique_uuid, user_id, chat_id, prompt, "", "", 0))
    conn.commit()
    
    job = q.enqueue(call_generation, prompt, chat_id, unique_uuid)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    