# Подключение к БД MySQL
import pymysql as pymysql
# HTTP запрос
import requests
# JSON
import json
# Пауза
import time

# Пароли
import secret


# Функция отправки GET запроса в API openweathermap
def requests_2_api(id_city, appid):
    # Запрос к API
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?id={id_city}&appid={appid}&units=metric").text
    # Вернуть ответа в JSON объекте
    return json.loads(response)


# Функция записи в БД
def write_2_bd(city_name, longitude, latitude, timezone, timestamp, country, sunrise_time, sunset_time, weather,
               weather_description, temperature, perceived_temperature, min_temperature, max_temperature, humidity,
               atmosphere_pressure, atmospheric_pressure_sea_level, atmospheric_pressure_ground_level,
               visibility, wind_speed, direction_wind, gust_wind,  rain_volume_one_hour, rain_volume_three_hour,
               snow_volume_one_hour, snow_volume_three_hour, cloudiness):

    # Подключение к БД
    connection = pymysql.connect(host=secret.host,
                                 user=secret.user_bd,
                                 password=secret.pass_bd,
                                 db=secret.schema,
                                 charset="utf8",
                                 cursorclass=pymysql.cursors.DictCursor)

    # Запись данных в БД
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO weather_data (city_name, longitude, latitude, timezone, timestamp, country, 
            sunrise_time, sunset_time, weather, weather_description, temperature, perceived_temperature, 
            min_temperature, max_temperature, humidity, atmosphere_pressure, atmospheric_pressure_sea_level, 
            atmospheric_pressure_ground_level, visibility, wind_speed, direction_wind, gust_wind, rain_volume_one_hour, 
            rain_volume_three_hour, snow_volume_one_hour, snow_volume_three_hour, cloudiness) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
            %s, %s)"""
            record = (city_name, longitude, latitude, timezone, timestamp, country, sunrise_time, sunset_time, weather,
               weather_description, temperature, perceived_temperature, min_temperature, max_temperature, humidity,
               atmosphere_pressure, atmospheric_pressure_sea_level, atmospheric_pressure_ground_level,
               visibility, wind_speed, direction_wind, gust_wind,  rain_volume_one_hour, rain_volume_three_hour,
               snow_volume_one_hour, snow_volume_three_hour, cloudiness)
            cursor.execute(sql, record)
            connection.commit()
    finally:
        # Закрыть соединение (Close connection).
        connection.close()


# Бесконечный цикл
while True:
    for id in secret.id_city:
        try:
            # Вызов функции отправки запроса на API
            response_from_api = requests_2_api(id, secret.appid)

            # Название города
            city_name = response_from_api["name"]
            # print(f"Имя обьекта: {city_name}")

            # Долгота
            longitude = response_from_api['coord']['lon']
            # print(f"Долгота: {longitude}")
            # Широта
            latitude = response_from_api['coord']['lat']
            # print(f"Широта: {latitude}")

            # Сдвиг в секундах от UTC
            timezone = response_from_api["timezone"]
            # print(f"Сдвиг в секундах от UTC: {timezone}")

            # Время расчета данных, unix, UTC
            timestamp = response_from_api["dt"]
            # print(f"Время расчета данных, unix, UTC: {datetime.fromtimestamp(timestamp)}")

            # Страна
            country = response_from_api["sys"]["country"]
            # print(f"Страна: {country}")

            # Время восхода, unix, UTC
            sunrise_time = response_from_api["sys"]["sunrise"]
            # print(f"Время восхода, unix, UTC: {datetime.fromtimestamp(sunrise_time)}")

            # Время заката, unix, UTC
            sunset_time = response_from_api["sys"]["sunset"]
            # print(f"Время заката, unix, UTC: {datetime.fromtimestamp(sunset_time)}")

            weather = ""
            weather_description = ""
            for item in (response_from_api["weather"]):
                # Погода
                weather = item["main"]
                # print(f"Погода: {weather}")
                # Описание погоды
                weather_description = item["description"]
                # print(f"Описание погоды: {weather}")

            # Температура
            temperature = response_from_api["main"]["temp"]
            # print(f"Температура: {temperature}")

            # температурный параметр объясняет человеческое восприятие погоды
            perceived_temperature = response_from_api["main"]["feels_like"]
            # print(f"температурный параметр объясняет человеческое восприятие погоды: {perceived_temperature}")

            # Минимальная температура на данный момент. Это минимальная наблюдаемая в настоящее время температура
            # (в пределах крупных мегаполисов и городских территорий)
            min_temperature = response_from_api["main"]["temp_min"]
            # print(f"Минимальная температура на данный момент: {min_temperature}")

            # Максимальная температура на данный момент. Это максимальная наблюдаемая в настоящее время температура
            # (в пределах крупных мегаполисов и городских территорий)
            max_temperature = response_from_api["main"]["temp_max"]
            # print(f"Максимальная температура на данный момент: {max_temperature}")

            # Влажность, %
            humidity = response_from_api["main"]["humidity"]
            # print(f"Влажность, %: {humidity}")

            # Атмосферное давление (на уровне моря, если нет данных sea_level или grnd_level), гПа
            atmosphere_pressure = response_from_api["main"]["pressure"]
            # print(f"Атмосферное давление: {atmosphere_pressure}")

            # Атмосферное давление на уровне моря, гПа
            atmospheric_pressure_sea_level = response_from_api["main"]["sea_level"]
            # print(f"Атмосферное давление на уровне моря, гПа: {atmospheric_pressure_sea_level}")

            # Атмосферное давление на уровне земли, гПа
            atmospheric_pressure_ground_level = response_from_api["main"]["grnd_level"]
            # print(f"Атмосферное давление на уровне земли, гПа: {atmospheric_pressure_ground_level}")

            # Видимость
            visibility = response_from_api["visibility"]
            # print(f"Видимость: {visibility}")

            # Скорость ветра. Единица измерения по умолчанию: метр / сек
            wind_speed = response_from_api["wind"]["speed"]
            # print(f"Скорость ветра. Единица измерения по умолчанию: метр / сек: {wind_speed}")

            # Направление ветра, градусы (метеорологические)
            direction_wind = response_from_api["wind"]["deg"]
            # print(f"Направление ветра, градусы (метеорологические): {direction_wind}")

            # Порыв ветра. Единица измерения по умолчанию: метр / сек
            gust_wind = response_from_api["wind"]["gust"]
            # print(f"Порыв ветра. Единица измерения по умолчанию: метр / сек: {gust_wind}")

            # Объем дождя за последний час, мм
            try:
                rain_volume_one_hour = response_from_api["rain"]["1h"]
                # print(f"Объем дождя за последний час, мм: {rain_volume_one_hour}")
            except KeyError:
                rain_volume_one_hour = 0

            # Объем дождя за последние 3 часа, мм
            try:
                rain_volume_three_hour = response_from_api["rain"]["3h"]
                # print(f"Объем дождя за последние 3 часа, мм: {rain_volume_three_hour}")
            except KeyError:
                rain_volume_three_hour = 0

            # Объем снега за 1 час
            try:
                snow_volume_one_hour = response_from_api["snow"]["1h"]
                # print(f"Объем снега за последний час: {snow_volume_one_hour}")
            except KeyError:
                snow_volume_one_hour = 0

            # Объем снега за последние 3 часа
            try:
                snow_volume_three_hour = response_from_api["snow"]["3h"]
                # print(f"Объем снега за последние 3 часа: {snow_volume_three_hour}")
            except KeyError:
                snow_volume_three_hour = 0

            # Облачность,%
            cloudiness = response_from_api["clouds"]["all"]
            # print(f"Облачность, %: {cloudiness}")

            # Вызов функции записи в БД
            write_2_bd(city_name, longitude, latitude, timezone, timestamp, country, sunrise_time, sunset_time, weather,
                       weather_description, temperature, perceived_temperature, min_temperature, max_temperature, humidity,
                       atmosphere_pressure, atmospheric_pressure_sea_level, atmospheric_pressure_ground_level,
                       visibility, wind_speed, direction_wind, gust_wind,  rain_volume_one_hour, rain_volume_three_hour,
                       snow_volume_one_hour, snow_volume_three_hour, cloudiness)

        except:
            pass

    # Системная пауза на 10 мин.
    print("Пазуа")
    time.sleep(600)
