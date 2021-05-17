# Write your MySQL query statement below
    
SELECT
    W2.id
FROM
    Weather W1, Weather W2
WHERE
    DATEDIFF(W2.recordDATE, W1.recordDate)=1 AND W2.Temperature > W1.Temperature;