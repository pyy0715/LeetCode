<h2>185. Department Top Three Salaries</h2><h3>Hard</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Employee</code></p>

<pre>+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| Id           | int     |
| Name         | varchar |
| Salary       | int     |
| DepartmentId | int     |
+--------------+---------+
Id is the primary key for this table.
Each row contains the ID, name, salary, and department of one employee.
</pre>

<p>&nbsp;</p>

<p>Table: <code>Department</code></p>

<pre>+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| Id          | int     |
| Name        | varchar |
+-------------+---------+
Id is the primary key for this table.
Each row contains the ID and the name of one department.
</pre>

<p>&nbsp;</p>

<p>Write an SQL query to find employees who earn the top three salaries in each of the departments.</p>

<p>Return the result table <strong>in any order</strong>.</p>

<p>The query result format is in the following example:</p>

<p>&nbsp;</p>

<pre>Employee table:
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+

Department table:
+----+-------+
| Id | Name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+

Result table:
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Joe      | 85000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+

In the IT department, Max earns the highest salary, both Randy and Joe earn the second-highest salary, and Will earns the third-highest salary. There are only two employees in the Sales department, Henry earns the highest salary while Sam earns the second highest salary.
</pre>
</div>