## 3. The With Clause ##

WITH playlist_summary AS (
    SELECT
        playlist.playlist_id,
        playlist.name AS playlist_name,
        COUNT(track.track_id) AS number_of_tracks,
        SUM(track.milliseconds / 1000) AS length_seconds
    FROM playlist
    LEFT JOIN playlist_track ON playlist.playlist_id = playlist_track.playlist_id
    LEFT JOIN track ON track.track_id = playlist_track.track_id
    GROUP BY playlist.playlist_id, playlist.name
)
SELECT
    playlist_id,
    playlist_name,
    number_of_tracks,
    length_seconds
FROM playlist_summary
ORDER BY playlist_id ASC;

## 4. Creating Views ##

DROP VIEW IF EXISTS chinook.customer_gt_90_dollars;

CREATE VIEW chinook.customer_gt_90_dollars AS
    SELECT *
    FROM chinook.customer
    WHERE customer_id IN (
        SELECT customer.customer_id
        FROM chinook.customer
        INNER JOIN chinook.invoice ON customer.customer_id = invoice.customer_id
        GROUP BY customer.customer_id
        HAVING SUM(invoice.total) > 90
    );
    
SELECT * FROM chinook.customer_gt_90_dollars;

## 5. Combining Rows With Union ##

SELECT *
FROM chinook.customer_usa
UNION
SELECT *
FROM chinook.customer_gt_90_dollars;

## 6. Combining Rows Using Intersect and Except ##

WITH customers_subset AS (
    SELECT 
        cu.support_rep_id,
        COUNT(*) AS customers_usa_gt_90
    FROM 
        customer_usa AS cu
        JOIN customer_gt_90_dollars AS cg ON cu.customer_id = cg.customer_id
    GROUP BY 
        cu.support_rep_id
)

SELECT 
    e.first_name || ' ' || e.last_name AS employee_name,
    COALESCE(cs.customers_usa_gt_90, 0) AS customers_usa_gt_90
FROM 
    employee AS e
    LEFT JOIN customers_subset AS cs ON e.employee_id = cs.support_rep_id
WHERE 
    e.title = 'Sales Support Agent'
ORDER BY 
    employee_name;

## 7. Multiple Named Subqueries ##

WITH
    customers_india AS
        (
        SELECT * FROM customer
        WHERE country = 'India'
        ),
    total_sales AS
        (
        SELECT 
            c.customer_id,
            c.first_name || ' ' || c.last_name AS customer_name,
            SUM(i.total) AS total_purchases
        FROM 
            customers_india AS c
            JOIN invoice AS i ON c.customer_id = i.customer_id
        GROUP BY 
            c.customer_id
        )
SELECT 
    customer_name,
    total_purchases
FROM 
    total_sales
ORDER BY 
    customer_name;

## 8. Challenge: Each Country's Best Customer ##

WITH
    customer_purchases AS (
        SELECT
            c.customer_id,
            c.first_name || ' ' || c.last_name AS customer_name,
            c.country,
            SUM(i.total) AS total_purchased
        FROM
            customer AS c
            JOIN invoice AS i ON c.customer_id = i.customer_id
        GROUP BY
            c.customer_id, c.country
    ),
    max_purchases AS (
        SELECT
            country,
            MAX(total_purchased) AS max_purchase
        FROM
            customer_purchases
        GROUP BY
            country
    ),
    top_customers AS (
        SELECT
            cp.customer_id,
            cp.customer_name,
            cp.country,
            cp.total_purchased
        FROM
            customer_purchases AS cp
            JOIN max_purchases AS mp ON cp.country = mp.country AND cp.total_purchased = mp.max_purchase
    )
SELECT
    tc.country,
    tc.customer_name,
    tc.total_purchased
FROM
    top_customers AS tc
ORDER BY
    tc.country;