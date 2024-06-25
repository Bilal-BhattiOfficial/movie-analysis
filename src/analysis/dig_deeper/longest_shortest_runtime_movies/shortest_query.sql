SELECT MIN(runtime) AS Shortest_runtime
FROM deduplicated_list
Where "type" = 'MOVIE';