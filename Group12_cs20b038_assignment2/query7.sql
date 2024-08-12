/*
     7.list of students enrolled in courses which doesnt have any prerequisites
*/

select stud.name, stud.rollNo,c.courseId
from student as stud,course as c,enrollment as e
where e.rollNo = stud.rollNo and e.courseId = c.courseId and 
	c.courseId NOT IN (select courseId from prerequisite)
