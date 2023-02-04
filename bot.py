from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.builtin import CommandStart

from config import TOKEN
from site_parse import parse_site
from utils import from_string_to_column
from settings import NO_GAPON_COMMENTS, NO_BAD_COMMENTS, BOT_START_MESSAGE

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply(BOT_START_MESSAGE)


@dp.message_handler()
async def echo(message: types.Message):
    "Отправка сообщений в бот"

    quantity_checked_pages = int(message.text)
    results_of_checked = parse_site(quantity_checked_pages)

    gapon_comments_id = from_string_to_column(results_of_checked[0])
    if gapon_comments_id:
        await message.answer(gapon_comments_id)
    else:
        await message.answer(NO_GAPON_COMMENTS)

    bad_comments = results_of_checked[1]

    if bad_comments:
        for comment in bad_comments:
            await message.answer({bad_comments[comment]})
    else:
        await message.answer(NO_BAD_COMMENTS)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
