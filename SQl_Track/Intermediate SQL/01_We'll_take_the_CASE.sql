/*Basic CASE statements*/

SELECT team_long_name,team_api_id
FROM teams_germany
WHERE team_long_name in ('FC Schalke 04','FC Bayern Munich');

SELECT 
	CASE WHEN hometeam_id = 10189 THEN 'FC Schalke 04'
        WHEN hometeam_id = 9823 THEN 'FC Bayern Munich'
         ELSE 'Other' END AS home_team,
	COUNT(id) AS total_matches
FROM matches_germany
GROUP BY home_team;

/*CASE statements comparing column values*/

SELECT 
	date,
	case when home_goal > away_goal then 'Home win!'
        when home_goal < away_goal then 'Home loss :(' 
        else 'Tie' end as outcome
FROM matches_spain;

SELECT 
	m.date,
	t.team_long_name AS opponent, 
	case when m.home_goal > m.away_goal then 'Home win!'
        when m.home_goal < m.away_goal then 'Home loss :('
        else 'Tie' end as outcome
FROM matches_spain AS m
left join teams_spain AS t
on m.awayteam_id = t.team_api_id;

SELECT 
	m.date,
	t.team_long_name AS opponent,
    case when m.home_goal >m.away_goal then 'Barcelona win!'
        when m.home_goal <m.away_goal then 'Barcelona loss :(' 
        else 'Tie' end as outcome 
FROM matches_spain AS m
LEFT JOIN teams_spain AS t 
ON m.awayteam_id = t.team_api_id
WHERE m.hometeam_id = 8634; 

SELECT  
	m.date,
	t.team_long_name AS opponent,
	case when m.home_goal <m.away_goal then 'Barcelona win!'
        when m.home_goal >m.away_goal then 'Barcelona loss :(' 
        else 'Tie' end as outcome 
FROM matches_spain AS m
LEFT JOIN teams_spain AS t 
ON m.hometeam_id = t.team_api_id
WHERE m.awayteam_id = 8634;

/*In CASE of rivalry*/

SELECT 
	date,
	case when  hometeam_id = 8634 then 'FC Barcelona' 
        else 'Real Madrid CF' end as home,
    case when awayteam_id = 8634 then 'FC Barcelona' 
        else 'Real Madrid CF' end as away
FROM matches_spain
WHERE (awayteam_id = 8634 OR hometeam_id = 8634)
      AND (awayteam_id = 8633 OR hometeam_id = 8633);
      
SELECT 
	date,
	CASE WHEN hometeam_id = 8634 THEN 'FC Barcelona' 
         ELSE 'Real Madrid CF' END as home,
	CASE WHEN awayteam_id = 8634 THEN 'FC Barcelona' 
         ELSE 'Real Madrid CF' END as away,
	case when home_goal > away_goal and hometeam_id = 8634 then 'Barcelona win!'
        WHEN home_goal > away_goal and hometeam_id = 8633 then 'Real Madrid win!'
        WHEN home_goal < away_goal and awayteam_id = 8634 then 'Barcelona win!'
        WHEN home_goal < away_goal and awayteam_id = 8633 then 'Real Madrid win!'
        else 'Tie!' end as outcome
FROM matches_spain
WHERE (awayteam_id = 8634 OR hometeam_id = 8634)
      AND (awayteam_id = 8633 OR hometeam_id = 8633);
      
/*Filtering your CASE statement*/

SELECT team_long_name,team_api_id
FROM teams_italy
WHERE team_long_name = 'Bologna';

SELECT 
	season,date,
    case when hometeam_id = 9857 and home_goal > away_goal then 'Bologna Win'
		 when awayteam_id = 9857 and away_goal > home_goal then 'Bologna Win' 
		end AS outcome
FROM matches_italy;

SELECT 
	season,
    date,
    home_goal,
    away_goal
FROM matches_italy
WHERE 
	case when hometeam_id = 9857 and home_goal > away_goal then 'Bologna Win'
		 when awayteam_id = 9857 and away_goal > home_goal then 'Bologna Win' 
		end IS NOT null;
    
/*COUNT using CASE WHEN*/

SELECT 
	c.name AS country,
	count(case when m.season = '2012/2013' 
        	then m.id ELSE null end) AS matches_2012_2013
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
group by country;

SELECT 
	c.name AS country,
	count(case when m.season = '2012/2013' then m.id end) AS matches_2012_2013,
	count(case when m.season = '2013/2014' then m.id end) AS matches_2013_2014,
	count(case when m.season = '2014/2015' then m.id end) AS matches_2014_2015
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
group by country;

/*COUNT and CASE WHEN with multiple conditions*/

SELECT 
	c.name AS country,
    sum(case when m.season = '2012/2013' AND m.home_goal > m.away_goal 
        THEN 1 ELSE 0 end) AS matches_2012_2013,
 	sum(case when m.season = '2013/2014' and m.home_goal > m.away_goal 
        THEN 1 else 0 end) AS matches_2013_2014,
	sum(case when m.season = '2014/2015' and m.home_goal > m.away_goal
        then 1 else 0 end) AS matches_2014_2015
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
GROUP BY country;

/*Calculating percent with CASE and AVG*/

SELECT 
    c.name AS country,
	count(case when m.home_goal > m.away_goal THEN m.id 
        END) AS home_wins,
	count(case when m.home_goal < m.away_goal THEN m.id 
        END) AS away_wins,
	count(case when m.home_goal = m.away_goal THEN m.id 
        END) AS ties
FROM country AS c
LEFT JOIN matches AS m
ON c.id = m.country_id
GROUP BY country;

SELECT 
	c.name AS country,
    avg(case when m.season='2013/2014' AND m.home_goal = m.away_goal THEN 1
			WHEN m.season='2013/2014' AND m.home_goal <> m.away_goal THEN 0
			END) AS ties_2013_2014,
	avg(case when m.season='2014/2015' AND m.home_goal = m.away_goal THEN 1
			WHEN m.season='2014/2015' AND m.home_goal <> m.away_goal THEN 0
			END) AS ties_2014_2015
FROM country AS c
LEFT JOIN matches AS m
ON c.id = m.country_id
GROUP BY country;

SELECT 
	c.name AS country,
    round(avg(CASE WHEN m.season='2013/2014' AND m.home_goal = m.away_goal THEN 1
			 WHEN m.season='2013/2014' AND m.home_goal != m.away_goal THEN 0
			 END),2) AS pct_ties_2013_2014,
	round(avg(CASE WHEN m.season='2014/2015' AND m.home_goal = m.away_goal THEN 1
			 WHEN m.season='2014/2015' AND m.home_goal != m.away_goal THEN 0
			 END),2) AS pct_ties_2014_2015
FROM country AS c
LEFT JOIN matches AS m
ON c.id = m.country_id
GROUP BY country;
