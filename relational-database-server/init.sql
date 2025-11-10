CREATE DATABASE IF NOT EXISTS studentdb;

USE studentdb;

CREATE TABLE IF NOT EXISTS students (
  id INT PRIMARY KEY AUTO_INCREMENT,
  student_id VARCHAR(10),
  fullname VARCHAR(100),
  dob DATE,
  major VARCHAR(50)
);

INSERT INTO students (student_id, fullname, dob, major) VALUES
('SV001', 'Nguyen Van A', '2003-05-12', 'Cloud Computing'),
('SV002', 'Tran Thi B', '2002-08-22', 'AI Engineering'),
('SV003', 'Le Van C', '2004-03-15', 'Software DevOps');
