-- Emp(eid : integer, ename : string, age : integer, salary : real)
-- Works(eid : integer, did : integer)
-- Dept(did : integer, budget : real, managerid : integer, dname:string)

-- 1) Find the name of employees who work in the hardware department
SELECT E.ename
FROM Emp E NATURAL JOIN Works W NATURAL JOIN Dept D
WHERE D.dname='Hardware';

-- 2) Find the name of the employee(s) in Hardware department who has the highest salary
SELECT E.ename
FROM Emp E NATURAL JOIN Works W NATURAL JOIN Dept D
WHERE D.dname='Hardware' AND E.salary = (SELECT MAX(salary) FROM Emp);

-- 3) Find the name and age of all employees who work in both Hardware and Software departments
SELECT E.ename, E.age
FROM Emp E NATURAL JOIN Works W NATURAL JOIN Dept D
WHERE D.dname='Hardware';
INTERSECT
SELECT E.ename, E.age
FROM Emp E NATURAL JOIN Works W NATURAL JOIN Dept D
WHERE D.dname='Software';


-- 4) Find the id of managers who control the largest total amounts of budget 
--    (note: a manager can manage multiple departments. The budget of these departments managed 
--    by the same manager should be summed up to calculate the total amounts of budget)

SELECT D.managerid
FROM Dept D
GROUP BY D.managerid
HAVING SUM(D.budget) >= ALL (SELECT SUM(D2.budget) FROM Dept D2 GROUP BY D2.managerid);

-- 5) Find the id of the managers who manage only the departments whose budget is at least 1 million dollars.

SELECT D.managerid
FROM Dept D
WHERE D.managerid NOT IN (SELECT D2.managerid FROM Dept D2 WHERE D2.budget < 1000000);

-- 6) Find the name of all employees whose salary exceeds the budget of each department that the employee works in.

SELECT E.ename
FROM Emp E NATURAL JOIN Works W NATURAL JOIN Dept D
GROUP BY E.ename, E.salary, E.eid
HAVING E.salary > ALL(
  SELECT D2.budget 
  FROM Emp E2 NATURAL JOIN Works W2 NATURAL JOIN Dept D2 
  WHERE E2.eid = E.eid);

-- 7)  Find the name of managers who manage the department of the largest budget [14pts].

SELECT E.ename
FROM Emp E NATURAL JOIN Works W NATURAL JOIN Dept D
WHERE D.managerid = E.eid AND D.budget >= (
  SELECT MAX(D2.budget)
  FROM Dept D2
);

-- 8) For each department, return the average salary of all employees working in this department

SELECT AVG(E.salary)
FROM Emp E NATURAL JOIN Works W NATURAL JOIN Dept D
GROUP BY D.did

-- 9) Find the name of the employees who work in more than 3 departments [14pts]. 

SELECT E.ename
FROM Emp E NATURAL JOIN Works W
WHERE 3 < ( SELECT COUNT(*) 
            FROM Emp E2 NATURAL JOIN Works W2
            WHERE E2.eid = E.eid);
