ALTER TABLE IF EXISTS aircrafts ADD COLUMN IF NOT EXISTS created_at timestamptz NOT NULL DEFAULT NOW();
ALTER TABLE IF EXISTS aircrafts ADD COLUMN IF NOT EXISTS updated_at timestamptz NOT NULL DEFAULT NOW();
COMMENT ON COLUMN aircrafts.created_at IS 'Дата создания';
COMMENT ON COLUMN aircrafts.updated_at IS 'Дата изменения';
ALTER TABLE IF EXISTS classes ADD COLUMN IF NOT EXISTS created_at timestamptz NOT NULL DEFAULT NOW();
ALTER TABLE IF EXISTS classes ADD COLUMN IF NOT EXISTS updated_at timestamptz NOT NULL DEFAULT NOW();
COMMENT ON COLUMN classes.created_at IS 'Дата создания';
COMMENT ON COLUMN classes.updated_at IS 'Дата изменения';
ALTER TABLE IF EXISTS seats ADD COLUMN IF NOT EXISTS created_at timestamptz NOT NULL DEFAULT NOW();
ALTER TABLE IF EXISTS seats ADD COLUMN IF NOT EXISTS updated_at timestamptz NOT NULL DEFAULT NOW();
COMMENT ON COLUMN seats.created_at IS 'Дата создания';
COMMENT ON COLUMN seats.updated_at IS 'Дата изменения';

