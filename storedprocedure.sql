create database office;
use office;
create table emp1(
	emp1_id INT PRIMARY KEY,
    emp1_name VARCHAR(40),
    dept_id  INT,
    dept_name VARCHAR(10)
);

INSERT INTO emp1 VALUES
(100,"sandy",20,"MCA"),
(101,"sweety",21,"MBA"),
(102,"candy",20,"BCA"),
(103,"banny",20,"MCA");

select * from emp1;




DELIMITER //

CREATE PROCEDURE get_emp1_dept(
    IN dept_id INT
)
BEGIN
    SELECT * 
    FROM emp1 
    WHERE emp1.dept_id = dept_id; 
END //
DELIMITER //
CALL get_emp1_department(1);


DELIMITER //
CREATE PROCEDURE get_emp1_marks(
	in minimum_marks INT
)
BEGIN
    SELECT * 
    FROM emp1 
    WHERE emp1.where marks >=minimum_marks; 
END //
DELIMITER //
CALL get_emp1_marks(90);


ALTER TABLE emp1
ADD marks INT;

UPDATE emp1
SET marks = 90
WHERE emp1_id = 100;

UPDATE emp1 SET marks = 90 WHERE emp1_id = 100;
UPDATE emp1 SET marks = 85 WHERE emp1_id = 101;
UPDATE emp1 SET marks = 75 WHERE emp1_id = 102;
UPDATE emp1 SET marks = 95 WHERE emp1_id = 103;

DELIMITER //

CREATE PROCEDURE marks_emp1(
    IN minimum_marks INT
)
BEGIN
    SELECT *
    FROM emp1
    WHERE marks >= minimum_marks;
END //

DELIMITER ;
CALL marks_emp1(80);

DELIMITER //
CREATE PROCEDURE count_employees1(
    OUT total INT
)
BEGIN
    SELECT COUNT(*) INTO total
    FROM emp1;
END //
DELIMITER ;
SET @employee_count = 0;
CALL count_employees1(@employee_count);
SELECT @employee_count;

DELIMITER //

CREATE PROCEDURE increase_number(
    INOUT num INT
)
BEGIN
    SET num = num + 10;
END //

DELIMITER ;
SET @number = 50;
CALL increase_number(@number);
SELECT @number;


