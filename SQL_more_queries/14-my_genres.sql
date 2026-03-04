-- SELECT all the genre of the show Dexter
SELECT name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE show_id = (
    SELECT id
    FROM tv_shows
    WHERE title = "Dexter"
)
ORDER BY tv_genres.name ASC;
