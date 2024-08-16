CREATE OR REPLACE FUNCTION udf_category_productions_count(category_name VARCHAR(50))
RETURNS VARCHAR 
AS 
$$
DECLARE
    production_count INTEGER;
BEGIN
    SELECT COUNT
	(*)
	INTO production_count
	FROM productions AS p
	JOIN categories_productions AS cp
		ON p.id = cp.production_id
	JOIN categories AS c
		ON c.id = cp.category_id
	WHERE c.name = category_name;

    RETURN 'Found ' || production_count || ' productions.';
END;
$$ LANGUAGE plpgsql;


-------------------------------------------------------------------

CREATE OR REPLACE PROCEDURE udp_awarded_production(production_title VARCHAR(70))
AS $$
BEGIN
    UPDATE actors
    SET awards = awards + 1
    WHERE id IN (
        SELECT a.id
        FROM actors a
        JOIN productions_actors AS pa
			ON a.id = pa.actor_id
        JOIN productions AS p
			ON p.id = pa.production_id
        WHERE p.title = production_title
    );
END;
$$ LANGUAGE plpgsql;