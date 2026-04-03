SELECT
    countries.name AS country_name,
    AVG(wines.ratings_average) AS avg_rating,
    COUNT(wines.id) AS wine_count,
    AVG(vintage_prices.avg_price) AS avg_price
FROM wines
JOIN regions ON wines.region_id = regions.id
JOIN countries ON regions.country_code = countries.code
LEFT JOIN (
    SELECT
        vintages.wine_id,
        AVG(vintages.price_euros) AS avg_price
    FROM vintages
    GROUP BY vintages.wine_id
) AS vintage_prices ON wines.id = vintage_prices.wine_id
GROUP BY countries.name
HAVING COUNT(wines.id) >= 50
ORDER BY avg_rating DESC;