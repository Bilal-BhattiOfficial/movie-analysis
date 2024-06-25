SELECT title, LENGTH(title) AS title_length
FROM deduplicated_list
ORDER BY title_length ASC
LIMIT 10;
