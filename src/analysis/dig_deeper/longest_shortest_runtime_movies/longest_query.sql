SELECT MAX(runtime) AS Longest_runtime
FROM deduplicated_list
Where "type" = 'MOVIE';