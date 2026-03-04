-- Show the score and the name attributes to it in desc order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
