-- Write a script that list all records of second_table
-- rows without a name value should not be listed
-- results should display score and name in decending order
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
