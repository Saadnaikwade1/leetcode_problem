SELECT 
  ROUND(
    SUM(CASE WHEN a.event_date = DATE_ADD(first_login, INTERVAL 1 DAY) THEN 1 ELSE 0 END)
    / COUNT(DISTINCT a1.player_id), 
  2) AS fraction
FROM 
  (SELECT player_id, MIN(event_date) AS first_login
   FROM Activity
   GROUP BY player_id) a1
JOIN 
  Activity a
ON a1.player_id = a.player_id;
