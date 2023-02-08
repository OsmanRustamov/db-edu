DROP TRIGGER IF EXISTS set_timestamp ON aircrafts;
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON aircrafts
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

DROP TRIGGER IF EXISTS set_timestamp ON classes;
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON classes
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

DROP TRIGGER IF EXISTS set_timestamp ON seats;
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON seats
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

