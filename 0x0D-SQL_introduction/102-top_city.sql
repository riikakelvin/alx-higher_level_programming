-- Imports in hbtn_0c_0 database this table dump
-- Displays Mean temp for July and August
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
