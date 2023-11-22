-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- uses a databse to lists all comedy in a table corresponding to all rows in another
SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_genre ON tv_show_genres.show_id = tv_genre.id
WHERE tv_genre.name = 'comedy'
GROUP BY title
ORDER BY title ASC;