SELECT
wineries.name AS winery_name,
countries.name AS country_name,
wines.ratings_average,
wines.ratings_count 
FROM wineries 
LEFT JOIN wines  ON wines.winery_id = wineries.id 
LEFT JOIN regions ON wines.region_id = regions.id 
LEFT JOIN countries ON regions.country_code = countries.code 
WHERE wines.ratings_average IS NOT NULL
AND wineries.name IS NOT NULL
ORDER BY wines.ratings_average   DESC , wines.ratings_count DESC 
LIMIT 10;