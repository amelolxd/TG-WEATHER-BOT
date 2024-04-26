import requests

open_weather_token = '104153bd2c2dc977e79ccbc1e07616f6'


def get_weather(city, api):
    emoji = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"}
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        zxc_weather = data["main"]["temp"]
        weatheremoji = data["weather"][0]["main"]
        if weatheremoji in emoji:
            smile = emoji[weatheremoji]
        return f"Погода в городе: {city.capitalize()}\nТемпература: {zxc_weather}C° {smile}\n"
    except Exception:
        return 'Проверьте названия города'


def get_weather2(city, api):
    emoji = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"}
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        zxc_weather = data["main"]["temp"]
        weatheremoji = data["weather"][0]["main"]
        wind = data["wind"]["speed"]
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        if weatheremoji in emoji:
            smile = emoji[weatheremoji]
        return f"Погода в городе: {city.capitalize()}\nТемпература: {zxc_weather}C° {smile}\n Ветер💨 {wind} м/c \n Давление {pressure} мм.рт.ст \n Влажность💧 {humidity} \n"
    except Exception:
        return 'Проверьте названия города'







def wind(city, api):
    r = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
    )
    data = r.json()
    return data["wind"]["speed"]

def get_pressure(city, api):
    r = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
    )
    data = r.json()
    return data["main"]["pressure"]

def humidity(city, api):
    r = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
    )
    data = r.json()
    return data["main"]["humidity"]

