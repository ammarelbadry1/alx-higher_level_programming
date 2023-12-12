-- This script lists all records of the table second_table of
-- the current database but don't list rows without a name value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
