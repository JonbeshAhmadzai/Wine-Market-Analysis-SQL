SELECT
    countries.name AS country_name,
    AVG(wines.ratings_average) AS avg_rating,
    SUM(wines.ratings_count) AS total_reviews
FROM wines
JOIN regions ON wines.region_id = regions.id
JOIN countries ON regions.country_code = countries.code
WHERE wines.ratings_average IS NOT NULL
GROUP BY countries.name
ORDER BY total_reviews DESC;