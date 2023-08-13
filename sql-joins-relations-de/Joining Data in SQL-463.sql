## 1. Introducing Joins ##

SELECT *
FROM facts
INNER JOIN cities ON facts.id = cities.facts_id
LIMIT 10;

## 2. Understanding Inner Joins ##

SELECT c.*, f.name AS country_name
FROM cities AS c
INNER JOIN facts AS f ON c.facts_id = f.id
LIMIT 5;

## 3. Practicing Inner Joins ##

SELECT f.name AS country, c.name AS capital_city
FROM facts AS f
INNER JOIN cities AS c ON c.facts_id = f.id
WHERE c.capital = 1;

## 4. Left Joins ##

SELECT f.name AS country, f.population
FROM facts AS f
LEFT JOIN cities AS c ON f.id = c.facts_id
WHERE c.name IS NULL;

## 6. Finding the Most Populous Capital Cities ##

SELECT c.name AS capital_city, f.name AS country, c.population
FROM cities AS c
JOIN facts AS f ON c.facts_id = f.id
WHERE c.capital = 1
ORDER BY c.population DESC
LIMIT 10;

## 7. Combining Joins with Subqueries ##

SELECT c.name AS capital_city, f.name AS country, c.population
FROM cities AS c
JOIN facts AS f ON c.facts_id = f.id
WHERE c.capital = 1
  AND c.population > 10000000
ORDER BY c.population DESC;

## 8. Challenge: Complex Query with Joins and Subqueries ##

SELECT f.name AS country,
       SUM(c.population) AS urban_pop,
       f.population AS total_pop,
       CAST(SUM(c.population) AS FLOAT) / f.population AS urban_pct
FROM facts AS f
JOIN cities AS c ON c.facts_id = f.id
GROUP BY country
HAVING urban_pct > 0.5
ORDER BY urban_pct ASC;