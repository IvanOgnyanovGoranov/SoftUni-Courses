-- Volunteers

SELECT name, phone_number, address, animal_id, department_id
FROM volunteers
ORDER BY name ASC, animal_id ASC, department_id ASC;

-- Animals Data

SELECT 
	a.name,
	a_t.animal_type,
	TO_CHAR(a.birthdate, 'DD.MM.YYYY') AS birthdate
FROM animals AS a
JOIN animal_types as a_t
	ON a.animal_type_id = a_t.id
ORDER BY a.name ASC;

-- Owners and Their Animals

SELECT 
	o.name,
	count(a.id) as count_of_animals
FROM animals AS a
JOIN owners AS o
	ON o.id = a.owner_id
GROUP BY o.name
ORDER BY count_of_animals DESC, o.name
LIMIT 5;

-- Owners, Animals and cages

SELECT 
	CONCAT(o.name, ' - ', a.name) AS "owners - animals",
	o.phone_number,
	ac.cage_id
FROM owners AS o
JOIN animals AS a
	ON o.id = a.owner_id
JOIN animals_cages AS ac
	ON a.id = ac.animal_id
JOIN animal_types AS at
	ON a.animal_type_id = at.id
WHERE at.animal_type = 'Mammals'
ORDER BY o.name ASC, a.name DESC;

-- Volunteers in Sofia

SELECT 
	v.name,
	v.phone_number,
	TRIM(BOTH ' , ' FROM REGEXP_REPLACE(REPLACE(v.address, 'Sofia', ''), ',+', ',')) AS address
FROM volunteers as v
JOIN volunteers_departments AS vd
	ON v.department_id = vd.id
WHERE vd.department_name = 'Education program assistant' 
	AND v.address LIKE '%Sofia%'
ORDER BY v.name;

-- Animals for Adoption

SELECT 
	name as animal, 
	EXTRACT(YEAR FROM a.birthdate) AS birth_year,
	at.animal_type
FROM animals AS a
JOIN animal_types AS at
	ON a.animal_type_id = at.id
WHERE a.owner_id IS NULL AND at.animal_type != 'Birds' AND birthdate > '01/01/2017'
ORDER BY a.name;
	