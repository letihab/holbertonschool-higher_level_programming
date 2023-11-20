--List all records of the table in my MySQL server.
--ORDERED by descending
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;

