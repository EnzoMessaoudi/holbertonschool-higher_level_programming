-- Shwo the score and how many times they appears
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
