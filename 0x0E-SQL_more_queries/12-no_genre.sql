-- lists all shows contained in hbtn_0d_tvshows
SELECT title, tv_show_genres.genre_id FROM tv_shows
-- display: tv_shows.title - tv_show_genres.genre_id
-- excludes genre
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
-- sorted in ascending order
ORDER BY title, tv_show_genres.genre_id;
