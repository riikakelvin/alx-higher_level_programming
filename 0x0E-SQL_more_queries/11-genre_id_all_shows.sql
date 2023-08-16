-- Lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
-- display show title and genre
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
-- sorted in ascending order
ORDER BY tv_shows.title, tv_show_genres.genre_id;
