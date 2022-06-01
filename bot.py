from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5425880418:AAFSTaiEQcTvTA57iet0UyNdgHLVn9dPNZQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nВведите любое математическое выражение!")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, eval(msg.text))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)