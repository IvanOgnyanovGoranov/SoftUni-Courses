--find book titles

SELECT 
	title
FROM 
	books
WHERE
	SUBSTRING (title, 1, 3) = 'The'
ORDER BY 
	id;

-- replace titles

SELECT
REPLACE
	(title, 'The', '***')
FROM 
	books
WHERE
	SUBSTRING(title, 1, 3) = 'The'
ORDER BY 
	id;

-- triangles on bookshelves

SELECT
	id,
	(side*height)/2 AS area
FROM
	triangles
ORDER BY id;

--format costs

SELECT
	title,
	TRUNC(cost, 3) 
AS modified_price
FROM books
ORDER BY id;

-- year of birth

SELECT
	first_name,
	last_name,
	EXTRACT(year FROM born) AS year
FROM authors;

-- format the date of birth

SELECT
	last_name AS "Last Name",
	TO_CHAR(born, 'DD (Dy) Mon YYYY') AS date_of_birth
FROM authors;

--Harry Potter books

SELECT
	title
FROM books
WHERE title LIKE 'Harry Potter%'
ORDER BY id;