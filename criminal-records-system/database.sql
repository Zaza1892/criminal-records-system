-- Create Database
CREATE DATABASE criminal_records;
GO

USE criminal_records;
GO

 -- Profile Table
 CREATE TABLE Profile_table (
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    cell INT NOT NULL,
    email VARCHAR(50) NOT NULL,
    unit_num INT NOT NULL,
    estate_name VARCHAR(50) NOT NULL,
    street_name VARCHAR(50) NOT NULL,
    suburb VARCHAR(50) NOT NULL,
    town VARCHAR(50) NOT NULL
);

 -- Crime Table
 CREATE TABLE Crime_table (
    crime_id INT PRIMARY KEY NOT NULL,
    description VARCHAR(200) NOT NULL,
    date DATE NOT NULL,
    severity_level INT NOT NULL,
    person_id INT NOT NULL,
    log_date DATE NOT NULL,
    admin_id INT NOT NULL
);

 -- Admin Table
 CREATE TABLE Admin_table (
    id INT PRIMARY KEY NOT NULL,
    username VARCHAR(40) NOT NULL,
    password INT NOT NULL,
    name VARCHAR(40) NOT NULL,
    surname VARCHAR(40) NOT NULL,
    cell INT NOT NULL,
    email VARCHAR(60) NOT NULL,
    employee_id INT NOT NULL
);

 -- Sample Data
 
INSERT INTO Profile_table (
    id, name, surname, cell, email,
    unit_num, estate_name, street_name, suburb, town
)
VALUES (
    1, 'john', 'low', 0123456789, 'jon@gmail.com',
    11, 'CitySquare', 'florida', 'suburbia', 'town city'
);

INSERT INTO Crime_table (
    crime_id, description, date, severity_level,
    person_id, log_date, admin_id
)
VALUES (
    1, 'break in', '2023-02-02', 3,
    12, '2023-02-02', 22
);

INSERT INTO Admin_table (
    id, username, password, name, surname,
    cell, email, employee_id
)
VALUES (
    122, 'admin1', 1234, 'Steve', 'Stevensin',
    0987654321, 'steve@gmail.com', 45
);