-- list the number of records with the same scofre in second_table
SELECT score COUNT(*) AS 'number'FROM second_table GROUP BY score ORDER BY score DESC;
