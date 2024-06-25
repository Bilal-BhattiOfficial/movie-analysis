SELECT genres, COUNT(*) AS movie_count
FROM titles
WHERE "type" = 'MOVIE'
GROUP BY genres
ORDER BY movie_count ASC;
