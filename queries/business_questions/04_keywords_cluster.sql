SELECT
    wines.name AS wine_name,
    GROUP_CONCAT(DISTINCT keywords.name) AS matching_keywords,
    GROUP_CONCAT(DISTINCT keywords_wine.group_name) AS matching_groups,
    COUNT(DISTINCT keywords.name) AS matched_keyword_count
FROM keywords
JOIN keywords_wine ON keywords.id = keywords_wine.keyword_id
JOIN wines ON keywords_wine.wine_id = wines.id
WHERE keywords.name IN ('coffee', 'toast', 'green apple', 'cream', 'citrus')
  AND keywords_wine.count > 10
GROUP BY wines.id, wines.name
ORDER BY matched_keyword_count DESC, wines.name;