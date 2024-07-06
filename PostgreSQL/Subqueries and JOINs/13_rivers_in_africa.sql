SELECT
    c.country_name,
    r.river_name
FROM countries as c
LEFT JOIN countries_rivers as c_r ON c.country_code = c_r.country_code
LEFT JOIN rivers as r ON r.id = c_r.river_id
WHERE c.continent_code = 'AF'
ORDER BY c.country_name ASC
LIMIT 5;