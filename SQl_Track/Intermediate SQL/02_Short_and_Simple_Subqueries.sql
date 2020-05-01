/*Filtering using scalar subqueries*/

SELECT 
	3 * avg(home_goal + away_goal)
FROM matches_2013_2014;

SELECT 
	date,
	home_goal,
	away_goal
FROM  matches_2013_2014
WHERE (home_goal+away_goal) > 
       (SELECT 3 * AVG(home_goal + away_goal)
        FROM matches_2013_2014); 
        
/*Filtering using a subquery with a list*/

SELECT 
	team_long_name,team_short_name
FROM team
WHERE team_api_id not in
     (select DISTINCT hometeam_id  FROM match);
     
/*Filtering with more complex subquery conditions*/

SELECT
	team_long_name,
	team_short_name
FROM team
WHERE team_api_id in
	  (SELECT hometeam_id
       FROM match
       WHERE home_goal >= 8);
       
/*Joining Subqueries in FROM*/

SELECT 
	country_id, 
    id
FROM match
WHERE (home_goal + away_goal) >= 10;

SELECT
	name AS country_name,
    COUNT(*) AS matches
FROM country AS c
inner join (SELECT country_id, id 
           FROM match
           WHERE (home_goal + away_goal)>=10) AS sub
ON c.id = sub.country_id
GROUP BY country_name;

/*Building on Subqueries in FROM*/

SELECT
	country,
    date,
    home_goal,
    away_goal
FROM 
	(SELECT name AS country, 
     	    m.date, 
     		m.home_goal, 
     		m.away_goal,
           (m.home_goal + m.away_goal) AS total_goals
    FROM match AS m
    LEFT JOIN country AS c
    
/*Add a subquery to the SELECT clause*/

SELECT 
	l.name AS league,
    ROUND(avg(m.home_goal + m.away_goal), 2) AS avg_goals,
    (SELECT round(avg(home_goal + away_goal), 2) 
     FROM match
     where season ='2013/2014') AS overall_avg
FROM league AS l
LEFT JOIN match AS m
ON l.country_id = m.country_id
WHERE season ='2013/2014'
GROUP BY l.name;

/*Subqueries in Select for Calculations*/

SELECT
	l.name AS league,
	ROUND(avg(m.home_goal + m.away_goal),2) AS avg_goals,
	ROUND(AVG(m.home_goal+ m.away_goal)  - 
		(SELECT avg(home_goal + away_goal)
		 FROM match 
         WHERE season = '2013/2014'),2) AS diff
FROM league AS l
LEFT JOIN match AS m
ON l.country_id = m.country_id
WHERE season='2013/2014'
GROUP BY l.name;

/*ALL the Subqueries EVERYWHERE*/

SELECT 
	m.stage,
    ROUND(avg(m.home_goal + m.away_goal),2) AS avg_goals,
    ROUND((SELECT avg(home_goal + away_goal) 
           FROM match 
           WHERE season = '2012/2013'),2) AS overall
FROM match AS m
WHERE m.season = '2012/2013'
GROUP BY stage;

/*Add a subquery in FROM*/

