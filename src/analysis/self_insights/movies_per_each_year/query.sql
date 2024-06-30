WITH MovieCounts AS (
    SELECT  release_year, COUNT(*) AS num_movies
    FROM    deduplicated_list
    WHERE   type = 'MOVIE'  -- Consider only movies
    GROUP BY    release_year
)
SELECT *
FROM    MovieCounts
