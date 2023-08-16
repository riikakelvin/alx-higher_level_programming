-- lists all shows without the genre Comedy, in hbtn_0d_tvshows. database
-- Each record should display: tv_shows.title
SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.id NOT IN (
      SELECT tv_shows.id FROM tv_shows
      JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
      JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
      WHERE tv_genres.name = "Comedy" )
--  sorted in ascending order by the show title
ORDER BY tv_shows.title;

