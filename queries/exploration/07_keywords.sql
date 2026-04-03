SELECT
    wines.name AS wine_name,
    keywords.name AS keyword,
    keywords_wine.group_name
FROM keywords
JOIN keywords_wine ON keywords.id = keywords_wine.keyword_id
JOIN wines ON keywords_wine.wine_id = wines.id
WHERE keywords.name IN ('coffee', 'toast', 'green apple', 'cream', 'citrus')
AND keywords_wine.count > 10;