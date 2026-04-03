SELECT COUNT(*)
FROM wines w
LEFT JOIN wineries wr ON w.winery_id = wr.id
WHERE wr.id IS NULL;