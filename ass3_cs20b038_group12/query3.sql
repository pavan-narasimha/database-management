/*
    count of number of movies released in year 2016.
*/
select count(title)
from movie
where movie.release_date='2016'