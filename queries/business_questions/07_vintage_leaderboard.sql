SELECT
    vintages.year AS vintage_year,
    AVG(vintages.ratings_average) AS avg_rating
FROM vintages
WHERE vintages.ratings_average IS NOT NULL
GROUP BY vintages.year
ORDER BY avg_rating DESC;