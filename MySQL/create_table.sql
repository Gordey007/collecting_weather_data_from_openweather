CREATE TABLE openweather.weather_data (
  id INT NOT NULL AUTO_INCREMENT,
  city_name VARCHAR(100) NULL,
  longitude DOUBLE NULL,
  latitude DOUBLE NULL,
  timezone INT NULL,
  timestamp INT NULL,
  country VARCHAR(10) NULL,
  sunrise_time INT NULL,
  sunset_time INT NULL,
  weather VARCHAR(100) NULL,
  weather_description VARCHAR(500) NULL,
  temperature DOUBLE NULL,
  perceived_temperature DOUBLE NULL,
  min_temperature DOUBLE NULL,
  max_temperature DOUBLE NULL,
  humidity INT NULL,
  atmosphere_pressure INT NULL,
  atmospheric_pressure_sea_level INT NULL,
  atmospheric_pressure_ground_level INT NULL,
  visibility INT NULL,
  wind_speed DOUBLE NULL,
  direction_wind INT NULL,
  gust_wind DOUBLE NULL,
  rain_volume_one_hour  DOUBLE NULL,
  rain_volume_three_hour  DOUBLE NULL,
  snow_volume_one_hour  DOUBLE NULL,
  snow_volume_three_hour  DOUBLE NULL,
  cloudiness INT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;