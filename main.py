
from config import TELEGRAM_TOKEN
from aiogram import Bot, Dispatcher, types, executor
from neiro.text import get_response
from neiro.test import general_img

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def func_start(message: types.Message):
    await message.answer('Привет я нейронка для изображений на минималках')


@dp.message_handler()
async def hendle_message(message: types.Message):
    response_text = await get_response(message.text)
    print(response_text)
    await message.reply('Идет генерация, подождите')
    try:
        image_data = general_img(response_text)
        await message.reply_photo(photo=image_data)
    except Exception as e:
        await message.reply(f'Произошла ошибка {e}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)