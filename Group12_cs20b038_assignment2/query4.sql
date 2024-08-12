/*
    4.list of students and their number of credits in year 2001 odd sem
*/
select s.rollNo,s.name,sum(c.credits)
from student as s,enrollment as e,course as c
where e.rollNo=s.rollNo and e.sem='odd'
 and e.year='2001' and e.courseId=c.courseId
group by s.rollNo
order by s.name