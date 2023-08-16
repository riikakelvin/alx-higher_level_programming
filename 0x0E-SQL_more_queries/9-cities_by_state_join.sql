-- lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities
-- display cities.id - cities.name - states.name
JOIN states ON cities.state_id=states.id
-- list cities in ascending order
ORDER BY cities.id;
