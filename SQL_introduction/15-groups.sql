-- lists the number of records with the same in the table second_table
SELECT score, COUNT(*) AS NUMBER
FROM second_table
GROUP BY score
ORDER BY score DESC;