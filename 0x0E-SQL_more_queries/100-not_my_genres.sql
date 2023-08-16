-- uses the hbtn_0d_tvshows database to list all genres
-- unlkinked to DEXTER, display: tv_genres.name
SELECT name FROM tv_genres
WHERE tv_genres.id NOT IN (
      SELECT tv_genres.id FROM tv_genres
      JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
      JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
      WHERE tv_shows.title = "DEXTER" )
--  sorted in ascending order by the genre name
ORDER BY tv_genres.name;

