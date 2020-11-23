-- Set Operations
-- 10/29/2020

-- Two options:
  -- DISTINCT: Consider only unique values
  -- ALL: Consider all values (default)

SELECT AVG(DISTINCT salary) AS avg_sal
FROM Staff;

-- Find the name and age of the oldest sailor(s)
SELECT S.sname, S.age
FROM Sailors S
WHERE S.age = ( SELECT MAX (S2.age)
                FROM Sailors S2);

-- This is not correct because it will just return the max age with every sailor name in the table.
SELECT S.sname, MAX(S.age) as maxage
FROM Sailors S;

-- This would however work if we use group by.

-- Group by (for each)
-- GROUP BY groups rows of the same values into groups.
--  It is used with aggregate function sto group the result-set.
SELECT att1, att2, aggregate_func
FROM tables
WHERE qualification
GROUP BY att1, att2, attn;
-- The attributes in the SELECT clause that are not in the aggregate function must appear in the GROUP BY
-- clause.

-- Group by with join

-- Query: for each red boat, return its number of reservations.
SELECT B.bid, COUNT(*) AS numres
FROM Boats B NATURAL JOIN Reserves R
WHERE B.color='red'
GROUP BY B.bid;

-- HAVING clause:
-- Having is a condition clause for GROUP BY. Filters groups based on GROUP BY.
-- HAVING needs a GROUP BY.

-- For each department, return its average employee salary if it is more than $3000.

SELECT DeptID, AVG(Salary)
FROM Employee
GROUP BY DeptID
HAVING AVG(Salary) > 3000;


-- For each rating group that has more than 1 sailor, find the lowest rating of sailors

SELECT MIN(S.rating) AS min-rating
FROM Sailors S
GROUP BY S.rating
HAVING COUNT(*) > 1

-- Where filters individual records. Having is applied for groups.


SELECT B.bid, COUNT(*) AS rCount
FROM Boats B NATURAL JOIN Reserves R
GROUP BY B.bid
HAVING B.color='red';
-- DOES NOT WORK. We can only use having with attributes in the group by clause,
-- or an aggregate function.