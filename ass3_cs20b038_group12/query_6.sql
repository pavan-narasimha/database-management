select person.person_name
from person,crew
where person.Aadhar=crew.crew_id and crew.movie_num='44'