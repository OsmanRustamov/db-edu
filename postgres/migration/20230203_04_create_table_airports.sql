CREATE TABLE IF NOT EXISTS airports (
    airport_code CHAR(3) NOT NULL,
    name TEXT NOT NULL,
    city_id INTEGER NOT NULL,
    coordinates POINT NULL,
    timezone TEXT NOT NULL,
    created_at timestamptz NOT NULL DEFAULT NOW(),
    updated_at timestamptz NOT NULL DEFAULT NOW(),
    PRIMARY KEY (airport_code),
    FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE CASCADE,
);

COMMENT ON COLUMN airports.airport_code IS 'Код аэропорта';
COMMENT ON COLUMN airports.name IS 'Название аэропорта';
COMMENT ON COLUMN airports.city_id IS 'Город';
COMMENT ON COLUMN airports.coordinates IS 'Координаты аэропорта (долгота и широта)';
COMMENT ON COLUMN airports.timezone IS 'Часовой пояс аэропорта';
COMMENT ON COLUMN airports.created_at IS 'Дата создания';
COMMENT ON COLUMN airports.updated_at IS 'Дата изменения';

DROP TRIGGER IF EXISTS set_timestamp ON airports;
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON airports
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();
