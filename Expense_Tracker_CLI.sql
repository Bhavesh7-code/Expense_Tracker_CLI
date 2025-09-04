CREATE DATABASE expense_tracker_cli;
USE expense_tracker_cli;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10,2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    date DATE NOT NULL
);
SHOW TABLES;
