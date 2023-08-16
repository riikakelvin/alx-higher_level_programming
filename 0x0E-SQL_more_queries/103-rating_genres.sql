-- lists all genres in the database hbtn_0d_tvshows_rate by rating
-- Each record should display: tv_genres.name - rating sum
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_show_genres.show_id
GROUP BY tv_genres.name
-- sorted in descending order by their rating
ORDER BY rating DESC;
