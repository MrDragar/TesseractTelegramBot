from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.callbacks import PhotoLanguageCallback


def get_choosing_lang_keyboard(file_id: str) -> types.InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="Русский язык", callback_data=PhotoLanguageCallback(
            language='rus',
            file_id=file_id
        )
    )
    keyboard.button(
        text="Английский язык", callback_data=PhotoLanguageCallback(
            language='eng',
            file_id=file_id
        )
    )
    return keyboard.as_markup()
