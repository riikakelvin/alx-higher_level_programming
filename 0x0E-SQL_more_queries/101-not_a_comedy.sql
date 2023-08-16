-- lists all shows without the genre Comedy, in hbtn_0d_tvshows. database
-- Each record should display: tv_shows.title
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy')
--  sorted in ascending order by the show title
ORDER BY tv_shows.title;

