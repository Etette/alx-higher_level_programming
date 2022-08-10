-- Write script that lists all shows in hbtn_0d_tvshows
-- display tv_shows.title and tv_show_genre.genre_id in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
