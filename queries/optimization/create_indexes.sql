CREATE INDEX IF NOT EXISTS idx_wines_region_id ON wines(region_id);
CREATE INDEX IF NOT EXISTS idx_wines_winery_id ON wines(winery_id);
CREATE INDEX IF NOT EXISTS idx_regions_country_code ON regions(country_code);
CREATE INDEX IF NOT EXISTS idx_keywords_wine_wine_id ON keywords_wine(wine_id);
CREATE INDEX IF NOT EXISTS idx_keywords_wine_keyword_id ON keywords_wine(keyword_id);
CREATE INDEX IF NOT EXISTS idx_most_used_grapes_country_code ON most_used_grapes_per_country(country_code);
CREATE INDEX IF NOT EXISTS idx_most_used_grapes_grape_id ON most_used_grapes_per_country(grape_id);
CREATE INDEX IF NOT EXISTS idx_vintages_wine_id ON vintages(wine_id);
CREATE INDEX IF NOT EXISTS idx_wines_ratings_average ON wines(ratings_average);
CREATE INDEX IF NOT EXISTS idx_wines_ratings_count ON wines(ratings_count);
CREATE INDEX IF NOT EXISTS idx_vintages_year ON vintages(year);

