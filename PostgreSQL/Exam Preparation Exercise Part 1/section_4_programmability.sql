--Template
CREATE OR REPLACE FUNCTION name()
RETURNS type
AS
$$
    DECLARE ;
    BEGIN
        ;
        RETURN ;
    END;
$$
LANGUAGE plpgsql;


-- All Volunteers in a Department
CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(searched_volunteers_department VARCHAR(30))
RETURNS INTEGER 
AS
$$
    DECLARE volunteers_count INTEGER;
    BEGIN
        SELECT 
            COUNT(*)
            INTO volunteers_count
            FROM volunteers AS v
            JOIN volunteers_departments AS vd
                ON v.department_id = vd.id
            WHERE vd.department_name = searched_volunteers_department;
        RETURN volunteers_count;
    END;
$$
LANGUAGE plpgsql;


--Animals with owner or not
CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(animal_name VARCHAR(30), OUT result VARCHAR(30))
AS
$$ 
BEGIN
    SELECT 
	o.name
    INTO result
    FROM animals AS a
    JOIN owners AS o
        ON a.owner_id = o.id
    WHERE a.name = animal_name;
	
	IF result IS NULL THEN result := 'For adoption';
	END IF;
END;
$$
LANGUAGE plpgsql;



	