SELECT release_year, runtime, "type"
FROM    deduplicated_list
WHERE release_year IS NOT NULL AND runtime IS NOT NULL