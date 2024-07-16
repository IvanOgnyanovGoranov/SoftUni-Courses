SELECT
	MIN(avg_areas) AS min_average_area
FROM
	(
	SELECT
		AVG(area_in_sq_km) AS avg_areas
	FROM countries
	GROUP BY continent_code
	) 
    AS min_average_area;