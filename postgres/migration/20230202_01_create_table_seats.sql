CREATE TABLE IF NOT EXISTS seats (
    aircraft_code CHAR(3) NOT NULL,
    seat_no VARCHAR(4) NOT NULL,
    fare_conditions INTEGER NOT NULL,
    PRIMARY KEY (aircraft_code, seat_no),
    FOREIGN KEY (aircraft_code) REFERENCES aircrafts(aircraft_code) ON DELETE CASCADE,
    FOREIGN KEY (fare_conditions) REFERENCES classes(id) ON DELETE CASCADE
);

COMMENT ON COLUMN seats.aircraft_code IS 'Код самолета, IATA';
COMMENT ON COLUMN seats.seat_no IS 'Номер места';
COMMENT ON COLUMN seats.fare_conditions IS 'Идентификатор класса обслуживания';
