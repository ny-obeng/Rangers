-- Create the database
CREATE DATABASE plumbing_solutions_db;
USE plumbing_solutions_db;

-- 1. Clients table
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    contact_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(50),
    address TEXT
);

-- 2. Services table
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    price_rate DECIMAL(10, 2)
);

-- 3. Service Requests table
CREATE TABLE service_requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    service_id INT NOT NULL,
    request_date DATE NOT NULL,
    scheduled_date DATE,
    status VARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- 4. Employees table
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    role VARCHAR(100), -- e.g., Technician, Trainer
    email VARCHAR(255),
    phone VARCHAR(50)
);

-- 5. Assignments table (linking employees to service requests)
CREATE TABLE assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    employee_id INT NOT NULL,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- 6. Training Programs table
CREATE TABLE training_programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,
    program_name VARCHAR(255) NOT NULL,
    description TEXT,
    duration_weeks INT,
    start_date DATE
);

-- 7. Trainees table
CREATE TABLE trainees (
    trainee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(50)
);

-- 8. Enrollments table
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    trainee_id INT NOT NULL,
    program_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    status VARCHAR(50) DEFAULT 'Active',
    FOREIGN KEY (trainee_id) REFERENCES trainees(trainee_id),
    FOREIGN KEY (program_id) REFERENCES training_programs(program_id)
);
