import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType
from aiogram.utils import executor
import typing as tp
import asyncio

# delete history

# /start askdlj
# /find
# /find bot


from exceptions import NoResultsFound
import aiohttp


bot = Bot(token=os.environ['BOT_TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message) -> None:
    await message.reply(("Бот сохраняет аудио сообщения (формат)"
                         " и отправленные картинки, на которых содержатся лица \n" 
                         "Для просмотра последних n аудио отправьте команду \\audio -n \n"
                         "Для просмотра последних n картинок отправьте команду \\pics -n \n"))


@dp.message_handler(commands=['audio'])
async def show_audio(message: types.Message) -> None:
    await message.reply("asdasda")


@dp.message_handler(commands=['pics'])
async def show_pics(message: types.Message) -> None:
    await message.reply("asdasd")


@dp.message_handler(content_types=[ContentType.VOICE])
async def handle_message(message: types.Message) -> None:
    file = await message.voice.get_file()
    print(await message.voice.get_url())
    # await bot.download_file(file_path=file["file_path"], destination='/home/nadia/Desktop/audio_downloaded.ogg')
    await message.reply("audio")

    # print(os.getcwd())
    # print(file)
    # pros = asyncio.create_subprocess_exec(f'ffmpeg -i {path} ')


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
