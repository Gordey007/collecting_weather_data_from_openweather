#collecting_weather_data

Программа предназначена для сбора информации о погоде.

Посредствам API программа получает следующие значения:
* Температура;
* Минимальная температура на данный момент;
* Максимальная температура на данный момент;
* температурный параметр объясняет человеческое восприятие погоды;
* Влажность, %;
* Атмосферное давление;
* Атмосферное давление на уровне моря, гПа;
* Атмосферное давление на уровне земли, гПа;
* Скорость ветра. Единица измерения по умолчанию: метр/сек;
* Направление ветра, градусы (метеорологические);
* Порыв ветра. Единица измерения по умолчанию: метр/сек;
* Облачность,%;
* Время восхода, unix, UTC;
* Время заката, unix, UTC;
* Время расчета данных.

API предоставляет данные с переодичностью в 10 минут.

Далее программа записывает значения о погоде в БД MySQL.