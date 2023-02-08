-- create regions
CREATE TABLE IF NOT EXISTS regions (
    id SERIAL NOT NULL,
    name TEXT NOT NULL,
    created_at timestamptz NOT NULL DEFAULT NOW(),
    updated_at timestamptz NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id),
    UNIQUE (name)
);

COMMENT ON COLUMN regions.id IS 'Идентификатор региона';
COMMENT ON COLUMN regions.name IS 'Название региона';
COMMENT ON COLUMN regions.created_at IS 'Дата создания';
COMMENT ON COLUMN regions.updated_at IS 'Дата изменения';

DROP TRIGGER IF EXISTS set_timestamp ON regions;
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON regions
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

-- create cities
CREATE TABLE IF NOT EXISTS cities (
    id SERIAL NOT NULL,
    region_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    created_at timestamptz NOT NULL DEFAULT NOW(),
    updated_at timestamptz NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id),
    FOREIGN KEY (region_id) REFERENCES regions(id) ON DELETE CASCADE,
    UNIQUE (region_id, name)
);

COMMENT ON COLUMN cities.id IS 'Идентификатор города';
COMMENT ON COLUMN cities.name IS 'Название города';
COMMENT ON COLUMN cities.created_at IS 'Дата создания';
COMMENT ON COLUMN cities.updated_at IS 'Дата изменения';

DROP TRIGGER IF EXISTS set_timestamp ON cities;
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON cities
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();
