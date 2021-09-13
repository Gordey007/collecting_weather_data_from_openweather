select
	t.id,
    t.city,
    t.longitude,
    t.latitude,
    t.temperature,
    t.minimum_temperature,
    t.maximum_temperature,
    t.perceived_temperature,
    t.humidity,
    t.atmosphere_pressure,
    t.atmospheric_pressure_sea_level,
    t.atmospheric_pressure_ground_level,
    t.wind_speed,
    t.direction_wind,
    t.gust_wind,
    t.cloudiness,
	from_unixtime(t.sunrise_time,"%d.%m.%Y %h:%i:%s") sunrise_time,
    from_unixtime(t.sunset_time,"%d.%m.%Y %h:%i:%s") sunset_time,
    from_unixtime(t.timestamp,"%d.%m.%Y %h:%i:%s") timestamp
from openweather.weather_data t;