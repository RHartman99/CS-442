-- Nested Queries
-- 10/29/2020

SELECT
FROM
WHERE EXP IN/EXISTS [ANY/ALL] (SELECT FROM WHERE);

-- Statements that include a subquery usually take these formats:
-- - WHERE attribute_name [NOT] IN (subquery)
-- - WHERE [NOT] EXISTS (subquery)
-- - WHERE expression op [ANY | ALL] (subqery)

-- Find name of sailors who've reserved boat #103
-- The attributes in the expression of the outer query must be EXACTLY THE SAME
-- as the output of the subquery.
-- Ergo, this is incorrect:

SELECT S.sname
FROM Sailors S
WHERE S.sid IN (SELECT R.sid, R.day FROM Reserves R WHERE R.bid=103);

-- Exists: boolean that checks value existence
-- Returns true if the result is not empty.

SELECT S.sname
FROM Sailors S
WHERE EXISTS (SELECT *
              FROM Reserves R
              WHERE R.bid=103 AND S.sid=R.sid);

-- Now, the evaluation of the subquery is dependent on the main query.
-- This is just natural join of reserves and sailors.

-- ANY:
-- Existince quantifier...if any record in the table satisfies the operator

-- 5 < ANY[0,5,6] = TRUE 
-- 5 < ANY[0,5] = FALSE 
-- 5 = ANY[0,5] = TRUE
-- 5 <> ANY[0,5] = TRUE

-- ALL:

-- 5 < all[0,5,6] = false
-- 5 < all[6,10] = true
-- 5 = all[4,5] = false
-- 5 <> all[4,6] = true

-- Using these:

-- Find sailors whose rating is greater than the rating of at least one sailor who are older than 20.
SELECT *
FROM Sailors Sailors
WHERE S.rating > ANY (SELECT S2.rating
                      FROM Sailors S2
                      WHERE S2.age>20);

-- Find sailors whose rating is greater than all sailors who are older than 20.
SELECT *
FROM Sailors Sailors
WHERE S.rating > ALL (SELECT S2.rating
                      FROM Sailors S2
                      WHERE S2.age>20);

-- Find sailors who have the highest rating.

SELECT *
FROM Sailors S
WHERE S.rating > ALL (SELECT S2.rating FROM Sailors S2);
-- DOES NOT WORK!!!! > all will return nothing! Must use >=, you can never have a higher rating
-- than yourself.
-- You also 
