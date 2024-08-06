-- Find all Courses by Client’s Phone Number 

CREATE OR REPLACE FUNCTION fn_courses_by_client(phone_num VARCHAR(20))
RETURNS INTEGER
AS
$$
    DECLARE number_of_courses INTEGER;
    BEGIN
        SELECT
            COUNT(co.id)
			INTO number_of_courses
            FROM courses AS co
            JOIN clients AS cl
                ON co.client_id = cl.id
            WHERE cl.phone_number = phone_num;
        RETURN number_of_courses;
    END;
$$ 
LANGUAGE plpgsql;

-- Full Info for Address

CREATE TABLE search_results (
    id SERIAL PRIMARY KEY,
    address_name VARCHAR(50),
    full_name VARCHAR(100),
    level_of_bill VARCHAR(20),
    make VARCHAR(30),
    condition CHAR(1),
    category_name VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE sp_courses_by_address(address_name VARCHAR(100))
AS
$$
BEGIN
    TRUNCATE search_results;

    INSERT INTO search_results(
        address_name,
        full_name,
        level_of_bill,
        make,
        condition,
        category_name
    )

    SELECT
        a.name AS address_name,
        cl.full_name,
        CASE
            WHEN co.bill <= 20 THEN 'Low'
            WHEN co.bill <= 30 THEN 'Medium'
            ELSE 'High'
        END AS level_of_bill,
        ca.make,
        ca.condition,
        ctg.name AS category_name
    FROM addresses AS a
    JOIN courses AS co
        ON co.from_address_id = a.id
    JOIN clients AS cl
        ON co.client_id = cl.id
    JOIN cars AS ca
        ON co.car_id = ca.id
    JOIN categories AS ctg
        ON ca.category_id = ctg.id
    WHERE a.name = address_name
    ORDER BY ca.make, cl.full_name;
END;
$$
LANGUAGE plpgsql;