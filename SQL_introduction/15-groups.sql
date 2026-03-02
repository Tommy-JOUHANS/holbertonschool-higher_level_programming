-- Lists all scores and the number of records for each score in the table second_table of the database hbtn_0c_0
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;