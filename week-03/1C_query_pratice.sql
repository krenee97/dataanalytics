USE northwind;

-- Question 1: List product id, name and unitprice in ascending order by price
SELECT ProductID, ProductName, UnitPrice
FROM products
Order BY UnitPrice ASC;

-- Question 2: Products with at least 100 units on hand, descending order by price
SELECT ProductID, ProductName, UnitPrice, UnitInStock
FROM products
WHERE UnitInStock >=100
ORDER BY UnitPrice DESC;

-- Question 3: Same as Q2 but if same price, sort by product name ascending
SELECT ProductID, ProductName, UnitPrice, UnitInStock
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, ProductName ASC;

-- Question 4: Total number of distinct customers who have placed orders
SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;

-- Question 5: Distinct customers per country, largest to smallest
SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS CustomerCount
FROM orders
Group BY ShipCountry
ORDER BY CustomerCount DESC;

-- Question 6: Products wiht less than 25 units on hand but 1+ on order 
-- Ordered by unit or order (high to low), then product name
SELECT ProductID, ProductName, UnitInStock, UnitInOrder
FROM Products 
WHERE UnitInStock < 25 AND UnitOnOrder >= 1
ORDER BY UnitOnOrder DESC, ProductName ASC;

-- Question 7: Each job title and count of employees with that title
SELECT Title, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Title;

-- Question 8: Employee with monthly salary between $2000 and $2500
-- Order by job title
SELECT FirstName, LastName, Title, Salary
FROM Employees
WHERE Salary BETWEEN 2000 AND 2500
ORDER BY Title;



