use college;
 create table students(
 student_id INT primary key,
 name VARCHAR(50)
);
create table course(
 student_id INT primary key,
 name VARCHAR(50)
);


INSERT INTO students values
(101,"sandy"),
(102,"swetha"),
(103,"radha"),
(104,"chinnu");

INSERT INTO course values
(101,"java"),
(102,"python"),
(103,"c"),
(105,"c++");

SELECT * FROM students
INNER JOIN  course
ON students.student_id = course.student_id;


SELECT
    students.student_id,
    students.name,
    course.course name
FROM students
LEFT JOIN course
ON students.student_id = course.student_id;


SELECT
    students.student_id,
    students.name AS student_name,
    course.name AS course_name
FROM students
LEFT JOIN course
ON students.student_id = course.student_id;


SELECT
    students.student_id,
    students.name AS student_name,
    course.name AS course_name
FROM students
RIGHT JOIN course
ON students.student_id = course.student_id;


SELECT
    students.student_id,
    students.name AS student_name,
    course.name AS course_name
FROM students
LEFT JOIN course
ON students.student_id = course.student_id

UNION

SELECT
    students.student_id,
    students.name AS student_name,
    course.name AS course_name
FROM students
RIGHT JOIN course
ON students.student_id = course.student_id;

SELECT
    students.student_id,
    students.name AS student_name,
    course.name AS course_name
FROM students
CROSS JOIN course;

CREATE DATABASE employee;
use employee;
create table emp(
 emp_id INT primary key,
 name VARCHAR(50),
 salary INT
);

create table department(
 emp_id INT primary key,
 role VARCHAR(50)
);



INSERT INTO emp VALUES
(101,"sandy",20000),
(102,"swetha",30000),
(103,"radha",25000),
(104,"chinnu",35000);


INSERT INTO department VALUES
(101,"design"),
(102,"coding"),
(103,"testing"),
(105,"deploye");

SELECT * FROM emp
INNER JOIN  department
ON emp.emp_id = department.emp_id;

SELECT
    emp.emp_id,
    emp.name,
    emp.salary,
    department.role
FROM emp
LEFT JOIN department
ON emp.emp_id = department.emp_id;


SELECT
    emp.emp_id,
    emp.name,
    emp.salary,
    department.role
FROM emp
RIGHT JOIN department
ON emp.emp_id = department.emp_id;

SELECT
    emp.emp_id,
    emp.name,
    emp.salary,
    department.role
FROM emp
LEFT JOIN department
ON emp.emp_id = department.emp_id

UNION

SELECT
    emp.emp_id,
    emp.name,
    emp.salary,
    department.role
FROM emp
RIGHT JOIN department
ON emp.emp_id = department.emp_id;


SELECT
    emp.emp_id,
    emp.name,
    department.role
FROM emp
CROSS JOIN department;



