import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from getweather import get_weather, open_weather_token, wind, get_pressure, humidity, get_weather2
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7143705319:AAEhPCqtdbuyiD08aQJXS0rzou5SfLzhE6E")
dp = Dispatcher()
cities = []
currentcity = []
currentcity.append('')


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if len(currentcity[0]) == 0:

        kb = [
            [
                types.KeyboardButton(text="Погода"),
                types.KeyboardButton(text="Влажность"),
                types.KeyboardButton(text="Ветер"),
                types.KeyboardButton(text="Давление")
            ],
        ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True)
    else:

        kb = [
            [
                types.KeyboardButton(text="Погода"),
                types.KeyboardButton(text="Влажность"),
                types.KeyboardButton(text="Ветер"),
                types.KeyboardButton(text="Давление")
            ],
        ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True)

    await bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}! Я Weather bot. Напишите мне что-название города, и я пришлю это погоду!", reply_markup=keyboard)


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await bot.send_message(message.from_user.id, 'команды: /start, /help, /add название города, /delete название города, /weather название города')


@dp.message(F.text == "Погода")
async def cmd_weather(message: types.Message):
    if len(currentcity[0]) == 0:
        await message.reply('выберите или добавьте город')
    else:
        await message.reply(get_weather(currentcity[0], open_weather_token))


@dp.message(F.text == "Ветер")
async def cmd_wind(message: types.Message):
    if len(currentcity[0]) == 0:
        await message.reply('выберите или добавьте город')
    else:
        await message.reply(f'Ветер💨 в {currentcity[0]}: {wind(currentcity[0], open_weather_token)} м/с')


@dp.message(F.text == "Давление")
async def cmd_pressure(message: types.Message):
    if len(currentcity[0]) == 0:
        await message.reply('выберите или добавьте город')
    else:
        await message.reply(f'Давление в {currentcity[0]}: {get_pressure(currentcity[0], open_weather_token)} мм.рт.ст')


@dp.message(F.text == "Влажность")
async def cmd_humidity(message: types.Message):
    if len(currentcity[0]) == 0:
        await message.reply('выберите или добавьте город')
    else:
        await message.reply(f'Влажность💧 в {currentcity[0]}: {humidity(currentcity[0], open_weather_token)}')


@dp.message(Command("list"))
async def cmd_list(message: types.Message):
    if cities:
        builder = InlineKeyboardBuilder()

        for index in cities:
            builder.button(text=index, callback_data=index)

        return await message.answer("Ваши сохраненные города", reply_markup=builder.adjust(2).as_markup())
    else:
        return await message.answer('Добавьте город с помощью команды /add')


@dp.callback_query()
async def callback_in(callback: types.callback_query):
    currentcity[0] = callback.data

    return await callback.answer(text=f'Выбран город {callback.data}', show_alert=True)


@dp.message(Command("weather"))
async def cmd_weather2(message: types.Message):
    text = message.text.split('/weather ')[1].capitalize()
    await message.reply(get_weather2(text, open_weather_token))


@dp.message(Command("delete"))
async def cmd_delete(message: types.Message):
    text = message.text.split('/delete ')[1].capitalize()
    if text in cities:
        cities.remove(text)
        await message.reply(f'город {text} удален')
    else:
        await message.reply(f'города {text} нет в списке')
@dp.message(Command("add"))
async def cmd_addr(message: types.Message):
    text = message.text.split('/add ')[1].capitalize()
    xd = get_weather(text, open_weather_token)
    if xd != 'Проверьте названия города':
        if text in cities:
            await message.reply(f'Город {text} уже есть добавлен')

        else:
            cities.append(text)
            currentcity[0] = text
            await message.reply(f'Город {text} добавлен и выбран')
    else:
        await message.reply('Проверьте названия города')
        





async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

