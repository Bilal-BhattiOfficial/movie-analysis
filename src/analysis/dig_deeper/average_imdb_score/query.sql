SELECT  CASE
        WHEN imdb_votes <= 1000 THEN '0-1000'
        WHEN imdb_votes > 1000 AND imdb_votes <= 10000 THEN '1001-10000'
        WHEN imdb_votes > 10000 AND imdb_votes <= 40000 THEN '10001-40000'
        WHEN imdb_votes > 40000 AND imdb_votes <= 70000 THEN '40001-70000'
        WHEN imdb_votes > 70000 THEN '>70000'
        ELSE 'Unknown'
    END AS vote_range,
    COUNT(*) AS num_movies,
    AVG(imdb_score) AS avg_imdb_score
FROM    deduplicated_list
GROUP BY    vote_range
ORDER BY    vote_range;
