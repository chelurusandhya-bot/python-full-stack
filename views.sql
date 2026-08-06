use college;
select * from student;
insert into student values(105,"hello2",20,"cse"),
(106,"hello3",21,"csc"),
(108,"hello4",23,"cst");

CREATE VIEW student_view AS
SELECT name, department
FROM student;
 select * from student_view;

CREATE VIEW cse_department AS SELECT * FROM student where department = "cse";
select * from cse_department;


create database students;
use students;


create table toppers(
	name VARCHAR(50),
    marks INT,
    department VARCHAR(30)
);


INSERT INTO  toppers VALUES("sai",89,"MCA"),
("charry",90,"MCA"),
("swetha",95,"BCA");

SELECT * FROM toppers;
CREATE VIEW topper AS SELECT name,marks from toppers;

select * from topper;