--Insert
INSERT INTO actors (first_name, last_name, birthdate, height, awards, country_id)
SELECT 
    REVERSE(first_name),               
    REVERSE(last_name),                
    birthdate - INTERVAL '2 days',     
    COALESCE(height + 10, 10),         
    country_id,                        
    (SELECT id FROM countries WHERE name = 'Armenia')
FROM actors
WHERE id BETWEEN 10 AND 20;  

--Update
UPDATE productions_info
SET duration = duration + 
    CASE 
        WHEN id < 15 THEN 15
        WHEN id >= 20 THEN 20
        ELSE 0
    END
WHERE synopsis IS NULL
  AND (id < 15 OR id >= 20);

--Delete
DELETE FROM countries
WHERE id NOT IN (
    SELECT DISTINCT country_id
    FROM actors
    UNION
    SELECT DISTINCT country_id
    FROM productions
);