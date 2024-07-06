SELECT
	m_c.country_code,
	COUNT(m.mountain_range) AS mounatain_range_count
FROM
	mountains as m
JOIN 
	mountains_countries as m_c
	ON m_c.mountain_id = m.id
where 
	m_c.country_code IN ('US', 'RU', 'BG')
GROUP BY 
	m_c.country_code
ORDER BY 
	m_c.country_code;
