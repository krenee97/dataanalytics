USE northwind;

-- Question 1: Product names(s) of the most expensive products
SELECT ProcuctName, UnitPrice
FROM Products 
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM Products);

-- Questions 2: Products name(s) and category of the least expensive products
SELECT p.ProductName, p.UnitPrice, c.CategoryName
FROM Products p 
JOIN Categories c ON p.CategoryID = c.CategoryID
WHERE p.UnitPrice = (SELECT MIN(UnitPrice) FROM Products);

-- Question 3: Order id, ship name, ship address for orders via "Federal Shipping"
SELECT OrderID, ShipenName, ShipAddress
FROM Orders 
WHERE ShipVia = ( SELECT ShipperID FROM Shippers WHERE CompanyName = 'Federal Shipping');

-- Question 4: Order IDs that include "Sasquatch Ale"
SELECT OrderID
FROM `Order Details`
WHERE ProductID = ( SELECT ProdcutID FROM Products WHERE ProductName = 'Sasquatch Ale');

-- Question 5: Name of the employee that sold order 10266
SELECT FirstName, LastName
FROM Employees
WHERE EmployeeID = ( SELECT EmloyeeID FROM Orders WHERE OrderID = 10266);

-- Question 6: Name of the customer that brought order 10266
SELECT CompanyName, ContactName 
FROM Customers
WHERE CustomerID = ( SELECT CUstomerID FROM Orders WHERE OrderID = 10266);


