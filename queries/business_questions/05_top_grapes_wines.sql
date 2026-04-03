WITH top_3_grapes AS (
    SELECT
        grapes.id AS grape_id,
        grapes.name AS grape_name,
        SUM(most_used_grapes_per_country.wines_count) AS total_wines
    FROM most_used_grapes_per_country
    JOIN grapes
        ON most_used_grapes_per_country.grape_id = grapes.id
    GROUP BY grapes.id, grapes.name
    ORDER BY total_wines DESC
    LIMIT 3
),
ranked_wines AS (
    SELECT
        top_3_grapes.grape_name,
        wines.name AS wine_name,
        countries.name AS country_name,
        wines.ratings_average,
        wines.ratings_count,
        ROW_NUMBER() OVER (
            PARTITION BY top_3_grapes.grape_name
            ORDER BY wines.ratings_average DESC, wines.ratings_count DESC
        ) AS wine_rank
    FROM wines
    JOIN regions
        ON wines.region_id = regions.id
    JOIN countries
        ON regions.country_code = countries.code
    JOIN most_used_grapes_per_country
        ON countries.code = most_used_grapes_per_country.country_code
    JOIN top_3_grapes
        ON most_used_grapes_per_country.grape_id = top_3_grapes.grape_id
    WHERE wines.ratings_average IS NOT NULL
)
SELECT
    grape_name,
    wine_name,
    country_name,
    ratings_average,
    ratings_count
FROM ranked_wines
WHERE wine_rank <= 5
ORDER BY grape_name, wine_rank
LIMIT 5;