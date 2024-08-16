SELECT 
	   id, 
       name, 
       continent, 
       currency
FROM countries
WHERE continent = 'South America'
  AND (currency LIKE 'P%' OR currency LIKE 'U%')
ORDER BY currency DESC, 
         id ASC;


----------------------
--that is the wrong one

SELECT 
	   pi.id,
       p.title,
       pi.duration,
       ROUND(pi.budget, 1) AS budget,
       TO_CHAR(pi.release_date, 'MM-YY') AS release_date
FROM productions AS p
JOIN productions_info AS pi
	ON p.production_info_id = pi.id
WHERE pi.release_date BETWEEN DATE '2023-01-01' AND DATE '2024-12-31'
  AND pi.budget > 1500000.00
ORDER BY pi.budget ASC,
         pi.duration DESC,
         pi.id ASC
LIMIT 3;


------------------------------------------------------------------

SELECT
    CONCAT(a.first_name, ' ', a.last_name) AS full_name,
    CONCAT(LOWER(SUBSTR(a.first_name, 1, 1)), 
           SUBSTR(a.last_name, LENGTH(a.last_name) - 1, 2), 
           LENGTH(a.last_name), 
           '@sm-cast.com') AS email,
    a.awards
FROM actors AS a
LEFT JOIN productions_actors AS pa
    ON a.id = pa.actor_id
WHERE pa.actor_id IS NULL
ORDER BY a.awards DESC, a.id ASC;

--------------------------------------------------------

SELECT
    p.title,
    CASE
        WHEN pi.rating <= 3.50 THEN 'poor'
        WHEN pi.rating > 3.50 AND pi.rating <= 8.00 THEN 'good'
        ELSE 'excellent'
    END AS rating_classification,
    CASE
        WHEN pi.has_subtitles = TRUE THEN 'Bulgarian'
        ELSE 'N/A'
    END AS subtitles,
    COUNT(pa.actor_id) AS actors_count
FROM productions AS p
JOIN productions_info AS pi
    ON p.production_info_id = pi.id
LEFT JOIN productions_actors AS pa
    ON p.id = pa.production_id
GROUP BY p.title, pi.rating, pi.has_subtitles
ORDER BY rating_classification ASC, actors_count DESC, p.title ASC;