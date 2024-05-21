-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
SELECT state, max(value) AS max_temp
       FROM temperatures
       GROUP BY state
       ORDER BY state;
