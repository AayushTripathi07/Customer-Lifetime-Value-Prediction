CREATE DATABASE clv_db;
USE clv_db;
CREATE TABLE sales_transactions (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    order_amount DECIMAL(10,2)
);
INSERT INTO sales_transactions (customer_id, order_date, order_amount) VALUES
(101, '2024-01-10', 1200),
(101, '2024-01-11', 900),
(102, '2024-01-12', 500),
(102, '2024-01-13', 700),
(103, '2024-01-14', 1500),
(104, '2024-01-15', 300),
(104, '2024-01-20', 450),
(105, '2024-01-25', 2000),
(106, '2024-02-10', 800),
(107, '2024-02-15', 950),
(108, '2024-02-18', 1100),
(109, '2024-02-20', 600),
(110, '2024-02-25', 1400);
SELECT * FROM sales_transactions;

