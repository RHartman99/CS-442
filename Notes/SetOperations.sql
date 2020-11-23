-- Set Operations
-- 10/13/2020

-- Union        Intersection    Set difference
Subquery 1      Subquery 1      Subquery 1
UNION           INTERSECT       EXCEPT
Subquery 2      Subquery 2      Subquery 2;

-- Each subqueries must be a valid subquery (SELECT FROM block. WHERE is optional)
-- All 3 must be union compatible-both subqueries must have the same schema.

-- Operation 1: Union
-- Find ID of sailors who've reserved a red or a green boat

SELECT R.sid
FROM Boats B, Reserves R
WHERE R.bid=B.bid AND (B.color='red' OR B.color='green');
-- AND has higher priority than OR, will always be evaluated first.

-- Using union:

SELECT R.sid
FROM Boats B, Reserves R
WHERE R.bid=B.bid AND B.color='red'
UNION
SELECT R.sid
FROM Boats B, Reserves R
WHERE R.bid=B.bid AND B.color='green'


-- Operation 2: Intersection
-- Find ID of sailors who've reserved a red AND a green boat.

SELECT R.sid
FROM Boats B, Reserves R
WHERE R.bid=B.bid AND B.color='red'
INTERSECT
SELECT R.sid
FROM Boats B, Reserves R
WHERE R.bid=B.bid AND B.color='green'

-- Operation 3: Set difference
-- Find name of sailors who've reserved at least 2 different boats.
SELECT
FROM
WHERE