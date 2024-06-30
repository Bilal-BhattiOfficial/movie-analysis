WITH ActorMovieCounts AS (
    SELECT  dl.release_year, c.name AS actor, COUNT(*) AS movie_count,
        ROW_NUMBER() OVER (PARTITION BY dl.release_year ORDER BY COUNT(*) DESC) AS row_num
    FROM    deduplicated_list dl
    JOIN    credits c ON dl.id = c.id
    WHERE   c.role = 'ACTOR'
    GROUP BY    dl.release_year, c.name
)
SELECT release_year, actor, movie_count
FROM    ActorMovieCounts
WHERE   row_num = 1
ORDER BY   release_year ASC;
