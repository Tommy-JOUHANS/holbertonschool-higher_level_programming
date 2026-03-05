-- Import the database dump of hbtn_0d_tvshows
-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows -- Query to join tv_show_genres and count the number of shows linked to each genre
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
