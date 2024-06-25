CREATE TABLE deduplicated_list AS
SELECT
    t.id AS id,
    t.title AS title,
    t."type" AS type,
    t.description AS description,
    t.release_year AS release_year,
    t.age_certification AS age_certification,
    t.runtime AS runtime,
    r.imdb_id AS imdb_id,
    r.imdb_score AS imdb_score,
    r.imdb_votes AS imdb_votes
FROM
    titles t
JOIN
    ratings r ON t.imdb_id = r.imdb_id
GROUP BY
    t.id;
