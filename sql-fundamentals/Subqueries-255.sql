## 1. Writing More Complex Queries ##

SELECT Major, ShareWomen
FROM recent_grads
WHERE ShareWomen > (SELECT AVG(ShareWomen) FROM recent_grads);

## 2. Subqueries ##

SELECT Major, Unemployment_rate
FROM recent_grads
WHERE Unemployment_rate < (SELECT AVG(Unemployment_rate) FROM recent_grads);

## 3. Subquery in SELECT ##

SELECT COUNT(*) * 1.0 / (SELECT COUNT(*) FROM recent_grads) AS proportion_abv_avg
FROM recent_grads
WHERE ShareWomen > (SELECT AVG(ShareWomen) FROM recent_grads);

## 4. The IN Operator ##

SELECT Major_category, Major
FROM recent_grads
WHERE Major_category IN ('Business', 'Humanities & Liberal Arts', 'Education');

## 5. Returning Multiple Results in Subqueries ##

SELECT Major_category, Major
FROM recent_grads
WHERE Major_category IN (
  SELECT Major_category
  FROM recent_grads
  GROUP BY Major_category
  ORDER BY SUM(Total) DESC
  LIMIT 3
);

## 6. Building Complex Subqueries ##

SELECT AVG(CAST(Sample_size AS FLOAT) / Total) AS avg_ratio
FROM recent_grads;

## 7. Practice Integrating A Subquery With The Outer Query ##

SELECT Major, Major_category, (CAST(Sample_size AS FLOAT) / Total) AS ratio
FROM recent_grads
WHERE (CAST(Sample_size AS FLOAT) / Total) > (
  SELECT AVG(CAST(Sample_size AS FLOAT) / Total)
  FROM recent_grads
);