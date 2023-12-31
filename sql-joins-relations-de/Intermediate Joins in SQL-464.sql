## 2. Joining Three Tables ##

SELECT il.track_id,
       t.name AS track_name,
       mt.name AS track_type,
       il.unit_price,
       il.quantity
FROM invoice_line AS il
JOIN track AS t ON t.track_id = il.track_id
JOIN media_type AS mt ON mt.media_type_id = t.media_type_id
WHERE il.invoice_id = 4;

## 3. Joining More Than Three Tables ##

SELECT
    il.track_id,
    t.name AS track_name,
    a.name AS artist_name,
    mt.name AS track_type,
    il.unit_price,
    il.quantity
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN album al ON al.album_id = t.album_id
INNER JOIN artist a ON a.artist_id = al.artist_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
WHERE il.invoice_id = 4;

## 4. Combining Multiple Joins with Subqueries ##

SELECT
    al.title AS album,
    ar.name AS artist,
    COUNT(il.track_id) AS tracks_purchased
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN album al ON al.album_id = t.album_id
INNER JOIN artist ar ON ar.artist_id = al.artist_id
GROUP BY al.album_id
ORDER BY tracks_purchased DESC
LIMIT 5;

## 5. Recursive Joins ##

SELECT
    e1.first_name || ' ' || e1.last_name AS employee_name,
    e1.title AS employee_title,
    e2.first_name || ' ' || e2.last_name AS supervisor_name,
    e2.title AS supervisor_title
FROM employee e1
LEFT JOIN employee e2 ON e1.reports_to = e2.employee_id
ORDER BY employee_name;

## 6. Pattern Matching Using Like ##

SELECT
    first_name,
    last_name,
    phone
FROM
    customer
WHERE
    first_name LIKE '%Belle%';

## 7. Generating Columns With The Case Statement ##

SELECT
    first_name || ' ' || last_name AS customer_name,
    COUNT(*) AS number_of_purchases,
    SUM(total) AS total_spent,
    CASE
        WHEN SUM(total) < 40 THEN 'small spender'
        WHEN SUM(total) > 100 THEN 'big spender'
        ELSE 'regular'
    END AS customer_category
FROM
    invoice
    INNER JOIN customer ON invoice.customer_id = customer.customer_id
GROUP BY
    customer.customer_id
ORDER BY
    customer_name;