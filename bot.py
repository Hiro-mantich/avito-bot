import ssl
import certifi

import asyncio # для библиотека для поддержки асиннхронных функций
import logging #логи
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F

from app.handlers import router
from app.database.models import async_make_db #импорт функции создания БД, если еще не создана

# Создаем SSL контекст с использованием сертификатов из certifi
ssl_context = ssl.create_default_context(cafile=certifi.where())

load_dotenv()
bot = Bot(os.getenv('TOKEN')) # токен бота
dp = Dispatcher() #хз



async def main():
    await async_make_db()
    dp.include_router(router)
    await dp.start_polling(bot,ssl_context=ssl_context)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) #только на этапе разработки онли для дебага
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

