/*Union*/

select *
  from economies2010
    union
select *
  from economies2015
order by code,year;

/*union(2)*/

select country_code
from cities
	union
select code 
  from currencies
order by country_code;

/*Union all*/

SELECT code, year
  FROM economies
	union all
SELECT country_code,year
  FROM populations
ORDER BY code, year;

/*Intersect*/

SELECT code, year
  FROM economies
	intersect
SELECT country_code,year
  FROM populations
ORDER BY code, year;

/*Except*/

SELECT name
  FROM cities
	except
SELECT capital
  FROM countries
ORDER BY name;

/*Except(2)*/

select capital 
  from countries
	except
select name
  from cities
order by capital;

/*Semi Join*/

select code 
from countries 
where region like 'Middle East';

select distinct name
from languages
order by name;

select distinct name
from languages
where code in (select code 
               from countries 
               where region like 'Middle East')
order by name;

/*Diagnosing problems using anti-join*/

select count(*)
  from countries
where continent='Oceania';

select code,name
from countries
where continent='Oceania' and 
  code not in (select code from currencies);
  
/*Set theory challenge*/

select name
  from cities AS c1
  WHERE country_code IN
(   SELECT distinct e.code
    FROM economies AS e  
        union
    SELECT distinct c2.code
    FROM currencies as c2
    except
    SELECT p.country_code
    FROM populations as p
);
