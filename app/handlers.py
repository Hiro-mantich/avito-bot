from aiogram import F , Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InputFile,BufferedInputFile
import os
import asyncio

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from pyexpat.errors import messages

import app.keyboards as kb
import app.database.requests as rq

from parser import main_parser

import app.database.requests as rq

router = Router()

@router.message(CommandStart()) #Команда старт
async def cmd_start(message:Message):
    await message.reply(f"Приветствую, друг мой, {message.from_user.full_name}", reply_markup=kb.btns_main_menu)

stop_event = asyncio.Event()

@router.message(F.text == 'Start parsing')
async def start_parsing(message:Message):
    await message.answer('Bot STARTED parsing for product')
    while not stop_event.is_set():
        #await main_parser()
        await asyncio.sleep(1)
    await message.answer('Bot STOPED parsing for product')

@router.message(F.text == 'Stop parsing')
async def stop_parsing(message: Message):
    await message.answer('Stop parsing for orders')
    stop_event.set()  # Устанавливаем событие для остановки парсинга