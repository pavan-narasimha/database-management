/*
     3.list of number of students being advised by professor
    */
select count(s.rollNo),professor.name
from professor,student as s
where s.advisor=professor.empId
group by professor.name