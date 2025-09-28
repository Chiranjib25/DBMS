# Student Database - Basic Queries Project(V1)

A MySQL database project demonstrating **basic SQL queries** using a simple student table with three columns:  
- Student Name  
- Age  
- Marks  

## Project Description

This project creates a student database with Indian student names . It demonstrates **basic SELECT queries** in SQL to display all students and filter them by **marks** or **age**.



### Run in MySQL Command Line
CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    marks INT
);

-- Insert sample data
INSERT INTO students (name, age, marks) VALUES
('Rohit Sharma', 20, 85),
('Priya Das', 19, 72),
('Amit Kumar', 21, 90),
('Sneha Roy', 18, 65),
('Manoj Kalita', 22, 78);

-- Example queries for V1 (Basic Queries)

-- Show all students
SELECT * FROM students;

-- Show students with marks greater than 70
SELECT * FROM students WHERE marks > 70;

-- Show students with marks less than 70
SELECT * FROM students WHERE marks < 70;

-- Show students older than 20
SELECT * FROM students WHERE age > 20;

-- Show students younger than 20
SELECT * FROM students WHERE age < 20;
