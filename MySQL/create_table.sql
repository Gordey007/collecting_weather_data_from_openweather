CREATE TABLE openweather.weather_data (
  id INT NOT NULL AUTO_INCREMENT,
  city VARCHAR(100) NULL,
  longitude DOUBLE NULL,
  latitude DOUBLE NULL,
  temperature DOUBLE NULL,
  minimum_temperature DOUBLE NULL,
  maximum_temperature DOUBLE NULL,
  perceived_temperature DOUBLE NULL,
  humidity INT NULL,
  atmosphere_pressure INT NULL,
  atmospheric_pressure_sea_level INT NULL,
  atmospheric_pressure_ground_level INT NULL,
  wind_speed DOUBLE NULL,
  direction_wind INT NULL,
  gust_wind DOUBLE NULL,
  cloudiness INT NULL,
  sunrise_time INT NULL,
  sunset_time INT NULL,
  timestamp INT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;