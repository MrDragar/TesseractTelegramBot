from aiogram.filters.callback_data import CallbackData


class PhotoLanguageCallback(CallbackData, prefix="Lang", sep=";"):
    language: str
    file_id: str
