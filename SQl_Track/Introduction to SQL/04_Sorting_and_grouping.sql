/*Sorting single columns*/

select name 
from people 
order by name;

select name 
from people
order by birthdate;

select birthdate,name 
from people
order by birthdate;

/*Sorting single columns (2)*/

select title 
from films
where release_year in (2000,2012)
order by release_year;

select *
from films
where release_year <> 2015
order by duration;

select title,gross 
from films
where title like 'M%'
order by title;

/*Sorting single columns (DESC)*/

select imdb_score,film_id
from reviews
order by imdb_score desc;

select title 
from films
order by title desc;

select title,duration
from films
order by duration desc;

/*Sorting multiple columns*/

select birthdate ,name
from people
order by birthdate,name;

select release_year,duration,title
from films
order by release_year,duration;

select certification,release_year,title
from films
order by certification,release_year;

select name,birthdate
from people
order by name,birthdate;

/*GROUP BY practice*/

select release_year,count(*)
from films
group by release_year;

select release_year,avg(duration)
from films
group by release_year;

select release_year,max(budget)
from films
group by release_year;

select imdb_score,count(*)
from reviews
group by imdb_score;

/*GROUP BY practice (2)*/

select release_year,min(gross)
from films
group by release_year;

select language,sum(gross)
from films
group by language;

select country,sum(budget)
from films
group by country;

select release_year,country,max(budget)
from films
group by release_year,country
order by release_year,country;

select country,release_year,min(gross)
from films
group by release_year,country
order by country,release_year;

/*All together now*/

select release_year,budget,gross
from films;

select release_year,budget,gross
from films
where release_year>1990;

select release_year
from films
where release_year>1990
group by release_year;

select release_year ,avg(budget) as avg_budget,avg(gross) as avg_gross
from films
where release_year>1990
group by release_year;

select release_year ,avg(budget) as avg_budget,avg(gross) as avg_gross
from films
where release_year>1990
group by release_year
having avg(budget)>60000000;

select release_year ,avg(budget) as avg_budget,avg(gross) as avg_gross
from films
where release_year>1990
group by release_year
having avg(budget)>60000000
order by avg_gross desc;

/*All together now (2)*/

select country,avg(budget) as avg_budget,avg(gross) as avg_gross
from films
group by country
having count(*)>10
order by country
limit 5;
