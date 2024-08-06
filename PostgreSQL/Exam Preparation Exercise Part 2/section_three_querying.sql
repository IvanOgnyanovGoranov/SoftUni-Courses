-- Cars
SELECT
	make,
	model,
	condition
FROM cars
ORDER BY id;

-- Drivers and cars

SELECT
	d.first_name,
	d.last_name,
	c.make,
	c.model,
	c.mileage
FROM drivers AS d
JOIN cars_drivers AS cd
	ON d.id = cd.driver_id
JOIN cars AS c
	ON cd.car_id = c.id
WHERE c.mileage IS NOT NULL
ORDER BY c.mileage DESC, d.first_name;


-- Number of Courses for each car

SELECT
	ca.id AS car_id,
	ca.make,
	ca.mileage,
	COUNT(co.car_id) AS count_of_courses,
	ROUND(AVG(co.bill), 2) AS average_bill
FROM cars AS ca
LEFT JOIN courses AS co
	ON co.car_id = ca.id
GROUP BY ca.id
HAVING COUNT(co.car_id) <> 2
ORDER BY count_of_courses DESC, ca.id;

-- Regular Clients

SELECT
	cl.full_name,
	COUNT(co.car_id) AS count_of_cars,
	SUM(co.bill)
FROM clients AS cl
JOIN courses AS co
	ON cl.id = co.client_id
GROUP BY cl.full_name
HAVING SUBSTRING(cl.full_name, 2, 1) = 'a' AND COUNT(co.car_id) > 1
ORDER BY cl.full_name;

-- Full Information of Courses

SELECT
	a.name,
	CASE
        WHEN EXTRACT(HOUR FROM co.start) BETWEEN 6 AND 20 THEN 'Day'
        ELSE 'Night'
	END AS day_time,
	co.bill,
	cl.full_name,
	ca.make,
	ca.model,
	ctg.name AS category_name
FROM addresses AS a
JOIN courses as co
	ON co.from_address_id = a.id
JOIN clients AS cl
	ON co.client_id = cl.id
JOIN cars AS ca
	ON co.car_id = ca.id
JOIN categories AS ctg
	ON ca.category_id = ctg.id
ORDER BY co.id;

