SELECT 
wines.name AS wine_name,
wineries.name AS winery_name,
countries.name AS country_name,
wines.ratings_average ,
wines.ratings_count
FROM wines 
LEFT JOIN wineries ON wines.winery_id = wineries.id 
LEFT JOIN regions  ON wines.region_id  = regions.id 
LEFT JOIN countries  ON regions.country_code = countries.code 
WHERE wines.ratings_count  >= 35000
ORDER BY wines.ratings_average DESC , wines.ratings_count DESC 
LIMIT 10;