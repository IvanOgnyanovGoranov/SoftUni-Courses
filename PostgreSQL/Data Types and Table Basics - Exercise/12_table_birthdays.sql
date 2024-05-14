CREATE TABLE minions_birthdays(
	id serial PRIMARY KEY,
	name VARCHAR(50),
	date_of_birth DATE,
	age INTEGER,
	present VARCHAR(100),
	party TIMESTAMP WITH TIME ZONE
	);
