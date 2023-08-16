-- Lists all California cities in database, hbtn_0d_usa
-- list order ascending
SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id;

