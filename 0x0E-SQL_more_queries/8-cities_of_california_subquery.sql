-- list all cities of CA in DB
-- results must be sorted in ascending order
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY id ASC;
