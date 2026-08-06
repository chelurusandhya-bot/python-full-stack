CREATE DATABASE  student;
USE student;




CREATE table students(
	rollno INT,
    name VARCHAR(50),
    course VARCHAR(30)
);


SHOW TABLES;

describe students;
INSERT INTO students  VALUES
(101,'chinnu','python');

SELECT * FROM students;


create database college;
use college;

create table student(
        id INT,
        name VARCHAR(50),
        age INT,
        department VARCHAR(30)
);
DESC student;

INSERT INTO student VALUES
(101,"swetha",21,"MCA"),
(102,"sandhya",21,"MCA"),
(103,"sandy",21,"MCA"),
(105,"radhika",21,"MCA");
SELECT *FROM student;

ALTER TABLE students
MODIFY email INT;
DESC students;

ALTER TABLE students
RENAME COLUMN email TO email_id;
DESC students;
RENAME TABLE students TO student_details;

DROP TABLE student_details;
SELECT*FROM student_details;


SET autocommit = 0;

START TRANSACTION;
INSERT INTO student VALUES(107,'hello1',21,'AII');
SAVEPOINT sp1;
INSERT INTO student VALUES(108,'hello2',22,'AII');
ROLLBACK TO sp1;

COMMIT;
SELECT * FROM student;



