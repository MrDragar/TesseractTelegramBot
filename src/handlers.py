import asyncio
import tempfile

from PIL import Image
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from pytesseract import pytesseract

from src.callbacks import PhotoLanguageCallback
from src.keyboards import get_choosing_lang_keyboard

router = Router()
file_id_storage: dict[str, str] = {}


@router.message(Command("help"))
@router.message(CommandStart())
async def start(message: Message):
    await message.reply(
        text="Привет. Я помогу тебе извлечь текст из твоей картинки.\n"
             "Просто пришли мне фотографию и выбери язык."
    )


@router.message(F.photo)
async def choose_language(message: Message):
    file_unique_id = message.photo[-1].file_unique_id
    await message.answer(
        text="Выберите язык, на котором будет обрабатываться ваша фотография",
        reply_markup=get_choosing_lang_keyboard(file_unique_id)
    )
    file_id_storage[file_unique_id] = message.photo[-1].file_id


@router.callback_query(PhotoLanguageCallback.filter())
async def handle_photo(query: CallbackQuery, callback_data: PhotoLanguageCallback):
    file_id = file_id_storage.get(callback_data.file_id, None)
    if file_id is None:
        return query.message.reply(
            "Срок действия фотографии истёк. Пожалуйста, отправьте её заново"
        )

    file = await query.bot.get_file(file_id)
    file_path = file.file_path
    downloaded_file = await query.message.bot.download_file(file_path)
    with tempfile.NamedTemporaryFile(
            delete=True, suffix=".jpg",
            dir=tempfile.gettempdir()) as temp_file:
        temp_file_path = temp_file.name

        with open(temp_file_path, "wb") as f:
            read_file = await asyncio.to_thread(downloaded_file.read)
            await asyncio.to_thread(f.write, read_file)

        image = await asyncio.to_thread(Image.open, temp_file_path)
        recognized_text = await asyncio.to_thread(
            pytesseract.image_to_string, image, callback_data.language
        )

    await query.message.reply(f"Распознанный текст:\n\n{recognized_text}")

