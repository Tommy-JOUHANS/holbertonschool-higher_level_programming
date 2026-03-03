-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name -- Query to list all the cities from California
FROM cities
WHERE state_id = ( -- Query to get the id of California
      SELECT id
      FROM states
      WHERE name = "California")