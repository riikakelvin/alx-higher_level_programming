-- lists all shows from hbtn_0d_tvshows_rate by rating
-- Each record should display: tv_shows.title - rating sum
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_show_ratings.show_id
-- sorted in descending order by rating
ORDER BY rating DESC;

