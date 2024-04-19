use sys;
SELECT * FROM payments;
INSERT INTO payments VALUES (18, 200, '2024-04-30', 123, NULL);
UPDATE payments SET amount=210 WHERE payment_id=12;
DELETE FROM payments WHERE payment_id=18;
-- Funciones Agregadoras (Aggregate Functions)
SELECT * FROM payments;
SELECT COUNT(amount) AS 'Cantidad de pagos' FROM payments;
SELECT MAX(amount) FROM payments;
SELECT MIN(amount) FROM payments;
SELECT SUM(amount) FROM payments;
SELECT AVG(amount) FROM payments;

SELECT * FROM payments WHERE customer_id=1;
SELECT SUM(amount) FROM payments WHERE date LIKE '%2024-04-18%';
SELECT * FROM customers;
SELECT * FROM customers WHERE address LIKE 'Lomas%';
SELECT * FROM customers WHERE address='Lomas de los Altos 2109';

SELECT * FROM customers WHERE city IN ('Guadalajara', 'Berlin');

SELECT * FROM payments WHERE date BETWEEN '2024-04-20%' AND '2024-04-30%';
SELECT * FROM customers WHERE age BETWEEN 20 AND 25;
-- JOIN------------------------------------------------
SELECT c.name, c.address FROM customers as c;
SELECT p.payment_id, c.name, c.age, p.amount  FROM payments p JOIN customers c ON c.customer_id = p.customer_id;
-- -------------------------
SELECT c.name, SUM(p.amount) AS total_paid FROM payments p JOIN customers c ON c.customer_id = p.customer_id GROUP BY c.name;