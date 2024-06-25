--PART A 
CREATE TABLE 
    products (
        product_name VARCHAR (100)
    );

INSERT INTO 
    products
VALUES
    ('Broccoli'),
    ('Shampoo'),
    ('Toothpaste'),
    ('Candy');

--PART B

ALTER TABLE
    products
ADD COLUMN
    "id" SERIAL PRIMARY KEY;