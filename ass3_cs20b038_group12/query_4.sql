/*
     all production company names which done a movie in genre action.
*/
select production_company.company_name
from movie
inner join production_company
on movie.genre='1' and movie.production_company=production_company.company_id
group by company_name
