/*Simple filtering of numeric values*/

select * 
from films
where release_year='2016';

select count(*) 
from films 
where release_year<'2000';

select title,release_year 
from films
where release_year>2000;

/*Simple filtering of text*/

select * 
from films 
where language='French';

select name,birthdate 
from people 
where birthdate='1974-11-11' 

select count(*) 
from films 
where language='Hindi';

select * from films
where certification='R';

/*WHERE AND*/

select title,release_year 
from films
where language='Spanish' and release_year<2000;

select * 
from films
where release_year>2000 and language='Spanish';

select * 
from films
where release_year>2000 and release_year<2010 and language='Spanish';

/*WHERE AND OR*/

select title,release_year 
from films
where release_year>=1990 and release_year<2000;

select title,release_year 
from films
where release_year>=1990 and release_year<2000
and language in ('French','Spanish');

select title,release_year 
from films
where release_year>=1990 and release_year<2000
and language in ('French','Spanish')
and gross>2000000;

/*BETWEEN*/

select title,release_year 
from films
where release_year between 1990 and 2000;

select title,release_year 
from films
where release_year between 1990 and 2000
and budget>100000000;

select title,release_year 
from films
where release_year between 1990 and 2000
and budget>100000000
and language='Spanish';

select title,release_year 
from films
where release_year between 1990 and 2000
and budget>100000000
and language in ('Spanish','French');

/*WHERE IN*/

select title,release_year 
from films 
where release_year in (1990,2000) 
and duration>120;

select title ,language
from films
where language in('English','Spanish','French');

select title,certification
from films
where certification in ('NC-17','R');

/*NULL and IS NULL*/

select name 
from people 
where deathdate is null;

select title 
from films 
where budget is null;

select count(*) 
from films
where language is null;

/*LIKE and NOT LIKE*/

select name 
from people 
where name like 'B%';

select name 
from people
where name like '_r%';

select name 
from people 
where name not like 'A%';
