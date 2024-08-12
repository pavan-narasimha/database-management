/* 
  (6)
  Display the Students Name,Roll Numbers and Courses Done greater than or equal to 2 in the year 2005 Even Semester
  and Sort them by Roll Numbers and CourseDone
*/
select convert(s.rollNo,unsigned) as RollNumbers,
s.name as Student,count(e.courseId) as CourseDone
from student AS s,enrollment AS e 
where s.rollNo=e.rollNo and e.sem='even' 
and e.year=2005
group by s.rollNo
having count(E.courseId) >= 2
order by RollNumbers,CourseDone;
