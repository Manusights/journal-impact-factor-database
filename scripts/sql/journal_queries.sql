-- Q1 journals by subject area
SELECT subject_area, COUNT(*) AS q1_count
FROM journals
WHERE quartile = 'Q1'
GROUP BY subject_area
ORDER BY q1_count DESC;

-- Publisher concentration
SELECT publisher, COUNT(*) AS n
FROM journals
GROUP BY publisher
ORDER BY n DESC
LIMIT 25;

-- High impact journals
SELECT journal_name, impact_factor
FROM journals
WHERE impact_factor >= 10
ORDER BY impact_factor DESC;
