/*Inner join*/

select * from cities;

select *
  from cities
    inner join countries
      on cities.country_code=countries.code;

SELECT cities.name as city,countries.name as country,region
FROM cities
  INNER JOIN countries
    ON cities.country_code = countries.code;
    
/*Inner join (2)*/

select c.code as country_code,name,year,inflation_rate
from countries as c
    inner join economies as e
        using(code);
    

select c.code,c.name,c.region,p.year,p.fertility_rate
from countries as c
    inner join populations as p
       on c.code=p.country_code;
       
/*Inner join (3)*/

select c.code,c.name,c.region,p.year,p.fertility_rate
from countries as c
    inner join populations as p
       on c.code=p.country_code;

SELECT c.code, name, c.region, e.year, fertility_rate,unemployment_rate
  FROM countries AS c
  INNER JOIN populations AS p
    ON c.code = p.country_code
    inner join economies as e
        using(code);
     
SELECT c.code, name, c.region, e.year, fertility_rate,unemployment_rate
  FROM countries AS c
  INNER JOIN populations AS p
    ON c.code = p.country_code
    inner join economies as e
        on c.code=e.code and p.year=e.year;
        
/*Inner join with using*/

select c.name as country,continent,l.name as language,official
from countries as c
    inner join languages as l
      using (code);
    
/*Self-join*/

select p1.country_code ,p1.size as size2010,p2.size as size2015
from populations as p1
    inner join populations as p2
        using(country_code);
     
select p1.country_code ,p1.size as size2010,p2.size as size2015
from populations as p1
    inner join populations as p2
        on p1.country_code=p2.country_code and p1.year=p2.year-5;

select p1.country_code ,p1.size as size2010,p2.size as size2015,(p2.size-p1.size)/p1.size*100.0 as growth_perc
from populations as p1
    inner join populations as p2
        on p1.country_code=p2.country_code and p1.year=p2.year-5;

/*Case when and then*/

SELECT name, continent, code, surface_area,
    CASE WHEN surface_area > 2000000 THEN 'large'
        WHEN surface_area> 350000 THEN 'medium'
        ELSE 'small' END
        AS geosize_group
FROM countries;

/*Inner challenge*/

SELECT country_code, size,
    -- 1. First case
    CASE WHEN size > 50000000 THEN 'large'
        -- 2. Second case
        WHEN size > 1000000 THEN 'medium'
        -- 3. Else clause + end
        ELSE 'small' END
        -- 4. Alias name (popsize_group)
        AS popsize_group
-- 5. From table
FROM populations
-- 6. Focus on 2015
WHERE year= 2015;

SELECT country_code, size,
    CASE WHEN size > 50000000 THEN 'large'
        WHEN size > 1000000 THEN 'medium'
        ELSE 'small' END
        AS popsize_group
-- 1. Into table
into pop_plus
FROM populations
WHERE year = 2015;
-- 2. Select all columns of pop_plus
select * from pop_plus;

select c.name,c.continent,c.geosize_group,p.popsize_group
from countries_plus as c
    inner join pop_plus as p
     using(code)
    order by geosize_group ;
