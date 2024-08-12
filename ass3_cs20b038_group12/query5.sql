select COUNT(language_name)
from movie,_language
where movie.movie_lang=_language.language_id and _language.language_name="telugu";