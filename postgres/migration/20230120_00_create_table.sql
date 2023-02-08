CREATE TABLE IF NOT EXISTS aircrafts (
    aircraft_code CHAR(3) NOT NULL,
    model TEXT NOT NULL,
    distance INTEGER NOT NULL,
    CHECK (distance > 0),
    PRIMARY KEY (aircraft_code)
);

COMMENT ON COLUMN aircrafts.aircraft_code IS 'Код самолета, IATA';
COMMENT ON COLUMN aircrafts.model IS 'Модель самолета';
COMMENT ON COLUMN aircrafts.distance IS 'Максимальная дальность полета, км';