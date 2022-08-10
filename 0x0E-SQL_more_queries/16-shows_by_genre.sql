-- List all shows and genres linked to that show
-- List all rows of a table linked to another table
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genre.id
ORDER BY title ASC, name ASC;
