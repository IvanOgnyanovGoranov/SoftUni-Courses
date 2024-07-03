SELECT 
	COUNT(b.booking_id) AS count
FROM customers AS c
JOIN bookings AS b 
USING (customer_id)
WHERE c.last_name = 'Hahn';

