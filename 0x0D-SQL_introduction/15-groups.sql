-- Grouping Records By It's Values

SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;

