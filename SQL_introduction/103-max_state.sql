-- Displays the max temperature of each state
SELECT state, MAX(value) AS max_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY state
ORDER BY max_temp DESC, state ASC
LIMIT 3;