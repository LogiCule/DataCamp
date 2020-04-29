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
