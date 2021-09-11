# Подключение к БД MySQL
import pymysql as pymysql
# HTTP запрос
import requests
import json
# Создание объекта SimpleNamespace, который обеспечивает доступ по атрибутам
from types import SimpleNamespace
# Дата и время
from datetime import datetime
# Пауза
import time
# Пароли
import secret

# Запрос к API
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?id={secret.id_city}&appid={secret.appid}&units=metric').text
# Сохранение ответа в JSON объект
json_object = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))

# Получение данных
# Температура
temperature = json_object.main.temp
print(f"Температура: {temperature}")

# Минимальная температура на данный момент. Это минимальная наблюдаемая в настоящее время температура
# (в пределах крупных мегаполисов и городских территорий)
minimum_temperature = json_object.main.temp_min
print(f"Минимальная температура на данный момент: {minimum_temperature}")

# Максимальная температура на данный момент. Это максимальная наблюдаемая в настоящее время температура
# (в пределах крупных мегаполисов и городских территорий)
maximum_temperature = json_object.main.temp_max
print(f"Максимальная температура на данный момент: {maximum_temperature}")

# температурный параметр объясняет человеческое восприятие погоды
perceived_temperature = json_object.main.feels_like
print(f"температурный параметр объясняет человеческое восприятие погоды: {perceived_temperature}")

# Влажность, %
humidity = json_object.main.humidity
print(f"Влажность, %: {humidity}")

# Атмосферное давление (на уровне моря, если нет данных sea_level или grnd_level), гПа
atmosphere_pressure = json_object.main.pressure
print(f"Атмосферное давление: {atmosphere_pressure}")

# Атмосферное давление на уровне моря, гПа
atmospheric_pressure_sea_level = json_object.main.sea_level
print(f"Атмосферное давление на уровне моря, гПа: {atmospheric_pressure_sea_level}")

# Атмосферное давление на уровне земли, гПа
atmospheric_pressure_ground_level = json_object.main.grnd_level
print(f"Атмосферное давление на уровне земли, гПа: {atmospheric_pressure_ground_level}")

# Скорость ветра. Единица измерения по умолчанию: метр / сек
wind_speed = json_object.wind.speed
print(f"Скорость ветра. Единица измерения по умолчанию: метр / сек: {wind_speed}")

# Направление ветра, градусы (метеорологические)
direction_wind = json_object.wind.deg
print(f"Направление ветра, градусы (метеорологические): {direction_wind}")

# Порыв ветра. Единица измерения по умолчанию: метр / сек
gust_wind = json_object.wind.gust
print(f"Порыв ветра. Единица измерения по умолчанию: метр / сек: {gust_wind}")

# Облачность,%
cloudiness = json_object.clouds.all
print(f"Облачность,%: {cloudiness}")

# Объем дождя за последний час, мм
# rain_volume_one_hour = json_object.rain['1h']

# Объем дождя за последние 3 часа, мм
# rain_volume_three_hour = json_object.rain['3h']

# Объем снега за 1 час, мм
# snow_volume_one_hour = json_object.snow['3h']

# Объем снега за последние 3 часа, мм
# snow_volume_three_hour = json_object.snow['3h']

# Время восхода, unix, UTC
sunrise_time = json_object.sys.sunrise
print(f"Время восхода, unix, UTC: {datetime.fromtimestamp(sunrise_time)}")

# Время заката, unix, UTC
sunset_time = json_object.sys.sunset
print(f"Время заката, unix, UTC: {datetime.fromtimestamp(sunset_time)}")

# Время расчета данных, unix, UTC
timestamp = json_object.dt
print(f"Время расчета данных, unix, UTC: {datetime.fromtimestamp(timestamp)}")

# Подключение к БД
connection = pymysql.connect(host=secret.host,
                             user=secret.user_bd,
                             password=secret.pass_bd,
                             db=secret.db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Бесконечный цикл
while True:
    # Запись данных в БД
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO weather_data_kms (temperature, minimum_temperature, maximum_temperature,
            perceived_temperature, humidity, atmosphere_pressure, atmospheric_pressure_sea_level,
            atmospheric_pressure_ground_level, wind_speed, direction_wind, gust_wind, cloudiness, sunrise_time,
            sunset_time, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            record = (temperature, minimum_temperature, maximum_temperature, perceived_temperature, humidity,
                      atmosphere_pressure, atmospheric_pressure_sea_level, atmospheric_pressure_ground_level, wind_speed,
                      direction_wind, gust_wind, cloudiness, sunrise_time, sunset_time, timestamp)
            cursor.execute(sql, record)
            connection.commit()
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

    # Системная пауза на 10 мин.
    # print("Пазуа")
    time.sleep(600)
