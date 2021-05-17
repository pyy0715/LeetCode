# Write your MySQL query statement below



SELECT C.Department, C.Employee, C.Salary
FROM
    (SELECT 
        A.Name AS Employee, 
        A.Salary, 
        A.Ranking,
        B.Name as Department
    FROM
        (SELECT 
            *, 
            DENSE_RANK() OVER(PARTITION BY DepartmentId ORDER BY Salary DESC) AS Ranking
        FROM Employee) A
        LEFT JOIN Department AS B
        ON A.DepartmentId = B.Id) AS C
WHERE C.Ranking <4;