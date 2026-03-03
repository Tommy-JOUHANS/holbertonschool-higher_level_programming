-- Import the database dump from hbtn_0d_tvshows
-- Script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_genres.name -- Query to join tv_shows, tv_show_genres and tv_genres to list all shows and genres linked to that show
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;