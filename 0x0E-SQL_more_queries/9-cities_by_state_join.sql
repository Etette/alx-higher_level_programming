-- List all cities in DB
-- each record should display cities.id - cities.name - states.name
-- results moust be sorted in ascending order from cities.id
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id
ORDER BY cities.id ASC;
