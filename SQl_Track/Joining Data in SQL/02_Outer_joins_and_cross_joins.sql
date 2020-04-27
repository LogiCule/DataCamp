/*Left Join*/

SELECT c1.name AS city, code, c2.name AS country,
       region, city_proper_pop
FROM cities AS c1
  INNER JOIN countries AS c2
    ON c1.country_code = c2.code
ORDER BY code desc;

SELECT c1.name AS city, code, c2.name AS country,
       region, city_proper_pop
FROM cities AS c1
  LEFT JOIN countries AS c2
    ON c1.country_code = c2.code
ORDER BY code desc;

/*Left join (2)*/


select c.name AS country, local_name, l.name AS language, percent
FROM countries AS c
  inner JOIN languages AS l
    using(code)
ORDER BY country desc;


select c.name AS country, local_name, l.name AS language, percent
FROM countries AS c
  left JOIN languages AS l
    using(code)
ORDER BY country desc;

/*Left join (3)*/

SELECT name,region,gdp_percapita
FROM countries AS c
  LEFT JOIN economies AS e
    using(code)
WHERE e.year = 2010;


SELECT region,avg(gdp_percapita) as avg_gdp
FROM countries AS c
  LEFT JOIN economies AS e
    using(code)
WHERE e.year = 2010
group by region;



SELECT region,avg(gdp_percapita) as avg_gdp
FROM countries AS c
  LEFT JOIN economies AS e
    using(code)
WHERE e.year = 2010
group by region
order by avg_gdp desc;

/*Right Join*/
SELECT cities.name AS city, urbanarea_pop, countries.name AS country,
       indep_year, languages.name AS language, percent
FROM languages
  RIGHT JOIN countries
    ON languages.code = countries.code
  RIGHT JOIN cities
    ON cities.country_code = countries.code
ORDER BY city, language;

/*Full join*/

SELECT name AS country, code, region, basic_unit
FROM countries
  FULL JOIN currencies
    USING (code)
WHERE region = 'North America' OR region IS null
ORDER BY region;

SELECT name AS country, code, region, basic_unit
FROM countries
  left JOIN currencies
    USING (code)
WHERE region = 'North America' OR region IS null
ORDER BY region;

SELECT name AS country, code, region, basic_unit
FROM countries
  inner JOIN currencies
    USING (code)
WHERE region = 'North America' OR region IS null
ORDER BY region;

/*Full Join(2)*/

SELECT countries.name, code, languages.name AS language
FROM languages
  full JOIN countries
    USING (code)
WHERE countries.name LIKE 'V%' OR countries.name IS null
ORDER BY countries.name;

SELECT countries.name, code, languages.name AS language
FROM languages
  left JOIN countries
    USING (code)
WHERE countries.name LIKE 'V%' OR countries.name IS null
ORDER BY countries.name;

SELECT countries.name, code, languages.name AS language
FROM languages
  inner JOIN countries
    USING (code)
WHERE countries.name LIKE 'V%' OR countries.name IS null
ORDER BY countries.name;

/*Full join (3)*/


SELECT c1.name AS country, region, l.name as language,
       basic_unit, frac_unit
FROM countries AS c1
  FULL JOIN languages AS l
    USING (code)
  FULL JOIN currencies AS c2
    USING (code)
WHERE region LIKE 'M%esia';

/*A table of two cities*/

SELECT c.name AS city, l.name AS language
FROM cities AS c        
  CROSS JOIN languages AS l
WHERE c.name LIKE 'Hyder%';

SELECT c.name AS city, l.name AS language
FROM cities AS c        
  inner JOIN languages AS l
    on c.country_code=l.code
WHERE c.name LIKE 'Hyder%';

/*Outer challenge*/

select c.name as country,region,life_expectancy as life_exp
from countries as c
  left join populations as p
    on p.country_code=c.code
where p.year=2010
order by life_exp
limit 5;
