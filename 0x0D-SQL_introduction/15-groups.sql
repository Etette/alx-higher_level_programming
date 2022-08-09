-- Write a script that list all records with the same score
-- result should display the score, number of records for this score with a label number
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
