-- Inport the database dump of hbtn_0d_tvshows
-- Script that uses the database hbtn_0d_tvshows database to list all genres of the shows Dexter
SELECT tv_genres.name -- Query to join tv_shows, tv_show_genres and tv_genres to list all genres of the show Dexter
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name;    
