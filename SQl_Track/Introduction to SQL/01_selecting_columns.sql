/*SELECTing single columns*/

select title
from films;

select release_year
from films;

select name 
from people;

/*SELECTing multiple columns*/

select title 
from films;

SELECT title,release_year
FROM films;

SELECT title, release_year,country 
FROM films;

select * 
from films;

/*SELECT DISTINCT*/

select distinct country 
from films;

select distinct certification f
rom films;

select distinct role from roles;

/*Practice with COUNT*/

select count(*) 
from people;

SELECT COUNT(*) 
FROM people where birthdate is not null;

SELECT COUNT( distinct birthdate) 
FROM people;

SELECT COUNT( distinct language)
FROM films;

SELECT COUNT( distinct country)
FROM films;
