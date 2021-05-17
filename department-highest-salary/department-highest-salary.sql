SELECT
    B.name AS Department,
    A.name AS Employee,
    A.Salary
FROM
    Employee A
    INNER JOIN Department B
    ON A.DepartmentId = B.Id
WHERE
    (A.DepartmentId , A.Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
    );