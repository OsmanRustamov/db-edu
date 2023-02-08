CREATE TABLE IF NOT EXISTS classes (
    id SERIAL NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (name)
);

COMMENT ON COLUMN classes.id IS 'Идентификатор класса обслуживания';
COMMENT ON COLUMN classes.name IS 'Название класса обслуживания';
