# 7032770656:AAFcQ0vZs3R1Qf4fkWnlD8BShhThppBd_1M
# ctrl + P
#! farruhdeveloper
#! https://t.me/farruhdeveloper


import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ContentType
from aiogram.utils import executor

from imageToText import image_to_text


logging.basicConfig(level=logging.INFO)

bot = Bot(token="7032770656:AAFcQ0vZs3R1Qf4fkWnlD8BShhThppBd_1M")
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply(
        "Assalomu Alaykum, menga rasm yuboring, va men undan text olib beraman"
    )


@dp.message_handler(content_types=ContentType.PHOTO)
async def handle_photo(message: types.Message):
    photo = message.photo[-1]
    file_info = await bot.get_file(photo.file_id)
    file_path = file_info.file_path
    image_filename = "user_image.png"
    await photo.download(destination_file=image_filename)

    text = image_to_text(image_filename)

    await message.reply(f"Here is  text from image:\n\n{text}")

    os.remove(image_filename)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
