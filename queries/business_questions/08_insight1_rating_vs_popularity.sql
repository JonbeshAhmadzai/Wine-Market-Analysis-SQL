SELECT
    wines.name,
    wines.ratings_average,
    wines.ratings_count
FROM wines
WHERE wines.ratings_average IS NOT NULL
ORDER BY wines.ratings_count DESC
LIMIT 20;