from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import  ReplyKeyboardBuilder, InlineKeyboardBuilder

btns_main_menu = ReplyKeyboardMarkup(keyboard =[
    [KeyboardButton(text ='Start parsing')],
    [KeyboardButton(text ='Stop parsing')],
    [KeyboardButton(text ='About')]],
        resize_keyboard = True,
        input_field_placefolder = 'Выберите действие')

async def btn_main_menu():
    keyboard = ReplyKeyboardBuilder()
    for btn in btns_main_menu:
        keyboard.add(KeyboardButton(text=btn))
    return keyboard.adjust(2).as_markup()