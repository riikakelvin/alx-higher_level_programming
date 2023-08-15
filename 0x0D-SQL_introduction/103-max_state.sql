-- Import in hbtn_0c_0 database this table dump, and displays max Temp
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;

