-- Import the database dump from hbtn_0d_tvshows
-- Script that lists all comedy shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title -- Query to join tv_shows, tv_show_genres and tv_genres to list all comedy shows
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;