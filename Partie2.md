-> First request : Find the turnover day by day since the first january to the 31 december 2019. The result
need to be sorted by the date of the command.

SELECT date, SUM(prod_price * prod_qty) AS ventes
FROM transactions
GROUP BY date ASC


-> Second request : Determine for each client during the 2019 year how many they buy from furniture and decoration

SELECT client_id, SUM(prod_price * prod_qty) AS ventes_meuble
FROM transactions AS tab1
INNER JOIN products_nomenclatures AS tab2 ON tab1.prod_id = tab2.prod_id
WHERE tab2.product_type = "MEUBLE"
GROUP BY client_id

UNION

SELECT client_id, SUM(prod_price * prod_qty) AS ventes_deco
FROM transactions AS tab1
INNER JOIN products_nomenclatures AS tab2 ON tab1.prod_id = tab2.prod_id
WHERE tab2.product_type = "DECO"
GROUP BY client_id