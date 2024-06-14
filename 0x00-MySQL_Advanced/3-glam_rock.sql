-- script that ranks country of bands,
-- ordered by the number of (non-unique) fans
SELECT origin, SUM(fans) as fans_count
FROM metal_bands
GROUP BY origin
ORDER BY fans_count DESC;
