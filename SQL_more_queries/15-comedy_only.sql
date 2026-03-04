-- SELECT all the title of series that are comedies
SELECT title
from tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE genre_id = (
    SELECT id
    FROM tv_genres
    WHERE name = "Comedy"
)
ORDER BY tv_shows.title ASC;
