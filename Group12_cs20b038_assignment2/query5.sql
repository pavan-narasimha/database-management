/*
    5.list of grades of a student in course teached by their faculty 
    advisor in between years 1995 and 2001
*/

select s.name as studentname,p.name as professorname,c.cname as coursename,e.grade as grade
from student as s,professor as p,course as c,enrollment as e,teaching as t
where s.advisor=p.empId and t.empId=p.empId and e.courseId = c.courseId and s.rollNo = e.rollNo and (e.grade='S' or 'A') and (e.year between '1995' and '2001')