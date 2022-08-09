-- Write a script that displays the max temperatures of each state
-- ordered by State name
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER By state ASC;
