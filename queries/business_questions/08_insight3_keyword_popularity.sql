SELECT
    keywords.name,
    SUM(keywords_wine.count) AS total_mentions
FROM keywords
JOIN keywords_wine ON keywords.id = keywords_wine.keyword_id
GROUP BY keywords.name
ORDER BY total_mentions DESC
LIMIT 20;