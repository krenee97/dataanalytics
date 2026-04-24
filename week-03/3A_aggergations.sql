USE Northwind;

-- Question 1a: Find the price of the cheapest item
SELECT Min(UnitPrice) AS CheatesptPrice 
FROM Produtcs;

-- Question 1b: Find the name of the product with the price
SELECT ProductName, UnitPrice
FROM Products 
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM Products);

-- Question 2: Average price of all items ( with ROUND)
SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM Products;

-- Question 3a: Find the price of the most expesive item
SELECT MAX(UnitPrice) AS MostExpensivePrice
FROM products;

-- Question 3b: Find the product name and supplier name for that price
SELECT p.ProductName, p.UnitPrice, s. ComapnyName AS SupplierName
FROM Produts p 
JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (SELECT MAX(UnitPrice) FROM Products);

-- Question 4: Total monthly payroll (sum of all salaries)
SELECT SUM(Salary) AS TotalMonthlyPayroll
FROM Employees;

-- Questions 5: Highest and lowest salary amounts
SELECT MAX(Salary) AS HighestSalary, MIN(Salary) AS LowestSalary
FROM Employees;

-- Question 6: Supplier name, supplier ID, and number of items they supply
SELECT s.SupplierID, s.CompanyName AS SupplierName, COUNT(p.ProductsID) AS ItemsSupplied
FROM Suppliers s 
JOIN Products p ON s.SupplierID = p.SupplieriD
GROUP BY s.SupplierID, s.CompanyName;

-- Question 7: Category names and average price per category
SELECT c.CategoryName, ROUND(AVG(p.UnitPrice), 2) AS AveragePrice
FROM Categories c 
JOIN Products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;

-- Question8 8: Suppliers who provide AT LEAST 5 items
SELECT s.CategoryName AS SupplierName, COUNT(p.ProductID) AS ItemSupplied
FROM Suppliers s 
JOIN Products p ON s.SupplierID
GROUP BY s.ComapnyName
HAVING COUNT(p.ProductID) >= 5;

-- Question 9: List products in inventroy with calculated inventory vaule 
-- (UnitPrice x UnitInStock), sorted by value descending, the product name
-- Exculde products not in stock
SELECT ProductID, ProductName, UnitPrice * UnitsInStock AS InventoryValue
FROM Products 
WHERE UNitsInStock > 0
ORDER BY InventroyValue DESC, ProductName ASC;
