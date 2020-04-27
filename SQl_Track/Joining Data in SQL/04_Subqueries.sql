/*Subquery inside where*/

select avg(life_expectancy)
  from populations
where year=2015;

select *
from populations
where life_expectancy>(select avg(life_expectancy)
  from populations
where year=2015)*1.15 
and year=2015;

/*Subquery inside where (2)*/

select name, country_code, urbanarea_pop
from cities
where name in
(select capital from countries)
ORDER BY urbanarea_pop DESC;

SELECT countries.name AS country, 
  (SELECT count(*)
   FROM cities
   WHERE countries.code = cities.country_code) AS cities_num
FROM countries
ORDER BY cities_num desc, country
LIMIT 9;

/*Subquery inside from*/

select code,count(*) as lang_num
  from languages
group by code;

select local_name,lang_num
  from countries,
  	(select code, count(*) as lang_num
  	 from languages
  	 group by code) AS subquery
  where countries.code =subquery.code
order by lang_num desc;

/*Advanced subquery*/

select name,continent ,inflation_rate
  from countries
  	inner join economies
    on countries.code=economies.code
where year=2015;

select max(inflation_rate) as max_inf
  FROM (
    select name,continent,inflation_rate from countries
    inner join economies
    using(code)
    where year=2015
      ) AS subquery
group by continent;

SELECT name, continent, inflation_rate
  FROM countries
	INNER JOIN economies
	using(code)
  WHERE year = 2015 and inflation_rate in (
        SELECT MAX(inflation_rate) AS max_inf
        FROM (
             SELECT name, continent, inflation_rate
             FROM countries
             INNER JOIN economies
             using(code)
             WHERE year = 2015) AS subquery
        GROUP BY continent);
        
/*Subquery challenge*/

SELECT code,inflation_rate, unemployment_rate
  FROM economies
  WHERE year = 2015 AND code not in
  	(SELECT code
  	 FROM countries
  	 WHERE (gov_form = 'Constitutional Monarchy' OR gov_form LIKE '%Republic%'))
ORDER BY inflation_rate;
