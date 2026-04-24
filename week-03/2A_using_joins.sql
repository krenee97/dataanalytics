USE northwind;

-- Question 1: Product id, name, unit price, and category name
-- ordered by category name, then product name
SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
FROM products p
JOIN Categories c ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName ASC, p.ProductName ASC;

-- Question 2: Product id, name ,unitprice, and supplier name
-- for products costing more than $75, ordered by product name
SELECT p.ProductID, p.ProductName, p.UnitPrice, s.CompanyName AS SupplierName
FROM Products 
JOIN Suppliers s ON p.SupplierID = s.SupplieriD
WHERE p.UnitPrice > 75
ORDER BY p.ProductName ASC;

-- Question 3: ProductID, name, unit price, category name, and supplier name
-- for every prodcut, ordered by product name
SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName, s.CompanyName AS SupplierName
FROM Products p 
JOIN Categories c ON p.CategoryID = c.CategoryID
JOIN Suppliers s ON p.SupplierID = s.SupplierID
ORDER BY p.ProductName ASC;

-- Question 4: Order id , ship name, ship address, adn shipping company name 
-- for orders shipped to Germany, ordered by shipper than ship name
SElECT o.OrderID, o.ShipName, o.ShipAdress, sh.ComapnyName AS Shipper
FROM Orders o
JOIN Shippers sh ON o.ShipVia = sh.ShipperID
Where o.ShipCountry = 'Germany'
ORDER BY sh.CompanyName ASC, o.ShipName ASC;

-- Question 5: Same as Q4 but group by ship name with count of orders
SELECT o.ShipName, sh.CompanyName AS Shipper, COUNT(*) AS OrderCount
FROM Orders o
JOIN Shippers sh ON o.ShipVia = sh.ShipperID
WHERE o.ShipCountry = 'Germany'
GROUP BY o.ShipName, sh.CompanyName
ORDER BY sh.ComapnyName ASC, o.ShipName ASC;

-- Question 6: OrderId, Order date, ship name, ship address
-- for all orders that inculde sasquatch Ale ( 3 table join)
SELECT o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
FROM Orders o 
JOIN `Order Details` od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale'
