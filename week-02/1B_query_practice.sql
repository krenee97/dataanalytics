USE northwind;

-- Question 1: List product id, product name, and unit proce of every product
SELECT ProductID, ProductName, UnitPrice
From Products;

-- Question 2: Products where unit price is $7.50 or less
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice <= 7.50;

-- Question 3: Products with no units on hand but 1 or more on backorder
SELECT ProductID, ProductName, UnitInStock, UnitOnOrder
FROM Products
WHERE UnitInStock = 0 AND UnitInOrder >= 1; 

-- Question 4a: How does the product table identify category?
SELECT ProductID, ProductName, CategoryID
FROM Products;

-- Question 4b: Find list of all categories 
SELECT CategoryID, CategoryName
FROM Categories;

-- Question 4c: List all seafood items (CategoryID = 8 in Northwind)
SELECT ProductID, ProductName
FROM Products
WHERE CategoryID = 8;

-- Question 5a: Find the SupplierID for Tokyo Traders
SELECT SupplierID, CompanyName
FROM Suppliers 
WHERE CompanyName = 'Tokyo Traders';

-- Question 5b: Find all products from Tokyo Traders ( SupplierID = 4)
SELECT ProductID, ProductName, SupplierID
FROM Products
WHERE SupplierID = 4;

-- Question 6a: How many employees work at Northwind?
SELECT COUNT(*) AS Total_Employees
FROM Employees;

-- Questions 6b: Employees with "mananger" in thier job title
SELECT FirstName, LastName, Title
FROM Employees 
WHERE Title LIKE '%manager%'



