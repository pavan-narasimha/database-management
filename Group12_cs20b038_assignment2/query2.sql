/*
   question2-selecting other courses in a department of a given course
*/
select course.courseID
from course 
where (course.courseID<>'340' and (course.deptNo= (select course.deptNo
                                   from course
                                   where course.courseID='340')
								  )
	  )