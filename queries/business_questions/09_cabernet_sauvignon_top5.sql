SELECT
    wines.name AS wine_name,
    countries.name AS country_name,
    wines.ratings_average,
    wines.ratings_count
FROM wines
JOIN regions
    ON wines.region_id = regions.id
JOIN countries
    ON regions.country_code = countries.code
WHERE wines.name LIKE '%Cabernet Sauvignon%'
  AND wines.ratings_average IS NOT NULL
ORDER BY
    wines.ratings_average DESC,
    wines.ratings_count DESC
LIMIT 5;