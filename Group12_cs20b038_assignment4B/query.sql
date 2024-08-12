/* 
	get the rollnumber , name of students in computer science department where the sex of student and the advisor is same
    whose start year is 2002
*/

create index n on student(year);
create index m on department(name);
explain 
select s.rollNo,s.name
from student as s,department as d, professor as p
where s.deptNo = deptId and d.name = "Comp. Sci" and p.empId = s.advisor and s.sex = p.sex
     and s.year = 2002