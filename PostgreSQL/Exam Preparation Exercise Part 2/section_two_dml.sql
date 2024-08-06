-- Insert
INSERT INTO clients 
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name,
    CONCAT('(088) 9999', id * 2) AS phone_number
FROM drivers
WHERE id BETWEEN 10 AND 20;

-- Update
UPDATE cars
SET condition = 'C'
WHERE (mileage > 800000 OR mileage IS NULL) AND year <= 2010 AND make <> 'Mercedes-Benz';

-- Delete
DELETE FROM clients
WHERE 
    LENGTH(full_name) > 3
    AND id NOT IN (
        SELECT client_id
        FROM courses
    );