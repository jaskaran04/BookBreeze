drop database org;
CREATE DATABASE IF NOT EXISTS ORG;
USE ORG;

CREATE TABLE Admin (
    Username varchar(20) PRIMARY KEY NOT NULL UNIQUE,
    Password varchar(20) NOT NULL
);

INSERT INTO Admin (Username, Password)
VALUES 
    ('admin1', 'password1'),
    ('admin2', 'password2'),
    ('admin3', 'password3'),
    ('admin4', 'password4'),
    ('admin5', 'password5');

CREATE TABLE Vendor (
    Vendor_ID int PRIMARY KEY auto_increment,
    Contact_number bigint NOT NULL UNIQUE,
    Vendor_Username varchar(20) UNIQUE,
    Vendor_Password varchar(100),
    Warehouse_no varchar(20) NOT NULL,
    Street_no varchar(20) NOT NULL,
    Zipcode integer NOT NULL,
    Email_ID varchar(40) NOT NULL UNIQUE,
  	Product_ID varchar(20),
  	Username varchar(20),
    FOREIGN KEY (Username) REFERENCES Admin(Username) on delete cascade
);


INSERT INTO Vendor (Vendor_Username, Vendor_Password, Contact_number, Warehouse_no, Street_no, Zipcode, Email_ID, Username)
VALUES 
    ('vendor1', 'password1', 1111111111, 'Warehouse 101', 'Oak Ave', 12345, 'vendor1@example.com', 'admin1'),
    ('vendor2', 'password2', 2222222222, 'Warehouse 202', 'Pine Ave', 23456, 'vendor2@example.com', 'admin2'),
    ('vendor3', 'password3', 3333333333, 'Warehouse 303', 'Maple Ave', 34567, 'vendor3@example.com','admin3'),
    ('vendor4', 'password4', 4444444444, 'Warehouse 404', 'Cedar Ave', 45678, 'vendor4@example.com', 'admin4'),
    ('vendor5', 'password5', 5555555555, 'Warehouse 505', 'Elm Ave', 56789, 'vendor5@example.com', 'admin5');
    
CREATE TABLE Vendor_Inventory (
	vendor_inventory_ID INT PRIMARY KEY auto_increment,
    Book_Name varchar(100),
    Vendor_ID int,
    Price DECIMAL(10, 2),
    Quantity INT,
    Genre VARCHAR(255),
    ratings int CHECK(Ratings >= 1 AND Ratings <= 5),
    FOREIGN KEY (Vendor_ID) REFERENCES Vendor(Vendor_ID) on delete cascade
);

INSERT INTO vendor_Inventory (Book_Name, Vendor_ID, Price, Quantity, Genre, ratings)
VALUES
    ('Book1', 1, 25.00, 100, 'Fiction', 5),
    ('Book2', 2, 20.00, 150, 'Fantasy', 4),
    ('Book3', 3, 30.00, 10, 'Mystery', 5),
    ('Book4', 4, 18.00, 120, 'Thriller', 4),
    ('Book5', 5, 22.00, 90, 'Science Fiction', 5);

CREATE TABLE Purchases_from (
	vendor_Inventory_ID INT,
    Username varchar(20),
    FOREIGN KEY (vendor_Inventory_ID) REFERENCES vendor_Inventory(vendor_inventory_ID) on delete cascade,
    FOREIGN KEY (Username) REFERENCES Admin(Username) on delete cascade,
    Date_of_purchase date NOT NULL,
    Time_of_purchase time NOT NULL,
    Amount INT,
    Quantity BIGINT NOT NULL,
    PRIMARY KEY (vendor_inventory_ID, Username, Date_of_purchase, Time_of_purchase)
);

INSERT INTO Purchases_from (vendor_Inventory_ID, Username, Date_of_purchase, Time_of_purchase, Amount, Quantity)
VALUES
	(1, 'admin1', '2024-03-15', '14:30:00', 2500, 100),
    (2, 'admin2', '2024-03-18', '11:45:00', 3000, 150),
    (3, 'admin3',  '2024-03-21', '09:15:00', 300, 10),
    (4, 'admin4', '2024-03-24',  '16:00:00', 3360, 120),
    (5, 'admin5', '2024-03-27', '13:20:00', 1980, 90);
    

UPDATE vendor_Inventory AS I 
JOIN Purchases_from AS P 
ON I.vendor_Inventory_ID = P.vendor_Inventory_ID
SET I.quantity = I.quantity - P.quantity;

CREATE TABLE Product (
    Product_ID int PRIMARY KEY auto_increment,
    Name varchar(20) NOT NULL,
    Genre varchar(50),
    Ratings integer NOT NULL CHECK (Ratings >= 1 AND Ratings <= 5),
    Price integer NOT NULL,
    Quantity integer NOT NULL DEFAULT 0,
    Vendor_ID int,  -- Added Vendor ID as foreign key
    Username varchar(20),
    FOREIGN KEY (Vendor_ID) REFERENCES Vendor(Vendor_ID) on delete cascade,
    FOREIGN KEY (Username) REFERENCES Admin(Username) on delete cascade
);

INSERT INTO Product (Name, Ratings, Price, Quantity, Vendor_ID, Username, Genre)
VALUES 
    ('Book1', 5, 25, 100, 1, 'admin1', 'Fiction'),
    ('Book2', 4, 20, 150, 2, 'admin2', 'Fantasy'),
    ('Book3', 5, 30, 10, 3, 'admin3', 'Mystery'),
    ('Book4', 4, 18, 120, 4, 'admin4', 'Thriller'),
    ('Book5', 5, 22, 90, 5, 'admin5', 'Science Fiction');
    
CREATE TABLE Delivery_Executive (
    Executive_ID int PRIMARY KEY NOT NULL auto_increment,
    username varchar(20) NOT NULL UNIQUE,
    password varchar(20) NOT NULL,
    First_Name varchar(20) NOT NULL,
    Last_Name varchar(20) NOT NULL,
    Email_ID varchar(40) NOT NULL UNIQUE,
    Contact_number bigint NOT NULL UNIQUE,
    House_No varchar(20) NOT NULL,
    Street_no varchar(20) NOT NULL,
    Zipcode integer NOT NULL,
    City varchar(20) -- Added attribute for City
);

-- Inserting into Delivery_Executive table
INSERT INTO Delivery_Executive (First_Name, Last_Name, Email_ID, Contact_number, House_No, Street_no, Zipcode, City, Username, Password)
VALUES 
    ('John', 'Doe', 'john.doe@example.com', 1234567890, 'Apt 101', '5th Avenue', 10001, 'New York', 'exec1', 'password1'),
    ('Jane', 'Smith', 'jane.smith@example.com', 9876543210, 'Suite B', 'Santa Monica Blvd', 90001, 'Los Angeles', 'exec2', 'password2'),
    ('Michael', 'Johnson', 'michael.johnson@example.com', 5555555555, 'Unit 3', 'Michigan Ave', 60601, 'Chicago', 'exec3', 'password3'),
    ('Emily', 'Brown', 'emily.brown@example.com', 4444444444, 'Apt 202', 'Main St', 77002, 'Houston', 'exec4', 'password4'),
    ('David', 'Martinez', 'david.martinez@example.com', 3333333333, 'Unit 5', 'Ocean Drive', 33101, 'New York', 'exec5', 'password5');
CREATE TABLE Users (
    Customer_ID varchar(20) PRIMARY KEY NOT NULL UNIQUE,
    Contact_number bigint NOT NULL UNIQUE,
    House_No varchar(20) NOT NULL,
    Street_no varchar(20) NOT NULL,
    Zipcode integer NOT NULL,
    Date_of_Birth varchar(20) NOT NULL,
    Email_ID varchar(40) NOT NULL UNIQUE,
    Age integer NOT NULL,
    Name_First_Name varchar(20) NOT NULL,
    Name_Last_Name varchar(20) NOT NULL,
    Coupons_Availability tinyint(1), -- Changed attribute name and datatype
    password varchar(20),
    CONSTRAINT chk_coupons CHECK (Coupons_Availability IN (0,1))
);

-- Inserting into Users table
INSERT INTO Users (Customer_ID, Contact_number, House_No, Street_no, Zipcode, Date_of_Birth, Email_ID, Age, Name_First_Name, Name_Last_Name, Coupons_Availability, password)
VALUES 
    ('CUS001', 1112223333, 'Apt 303', 'Maple Ave', 12345, '1990-05-15', 'user1@example.com', 31, 'Alice', 'Johnson', 1, 'pass1'),
    ('CUS002', 2223334444, 'Suite 202', 'Oak Ave', 23456, '1985-10-20', 'user2@example.com', 36, 'Bob', 'Smith', 1, 'pass2'),
    ('CUS003', 3334445555, 'Unit 101', 'Cedar Ave', 34567, '1978-03-25', 'user3@example.com', 43, 'Charlie', 'Brown', 0, 'pass3'),
    ('CUS004', 4445556666, 'Apt 404', 'Pine Ave', 45678, '1988-08-08', 'user4@example.com', 33, 'Diana', 'Garcia', 0, 'pass4'),
    ('CUS005', 5556667777, 'Suite 303', 'Elm Ave', 56789, '1995-12-12', 'user5@example.com', 26, 'Eva', 'Martinez', 1, 'pass5');

-- Update age for each user based on DOB
UPDATE Users
SET Age = TIMESTAMPDIFF(YEAR, STR_TO_DATE(Date_of_Birth, '%Y-%m-%d'), CURDATE());

CREATE TABLE Orders (
	Order_ID varchar(20),
    Date1 DATE NOT NULL,
    Time1 TIME NOT NULL,
    No_of_books INT NOT NULL DEFAULT 0,
    Product_ID int, 
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID) on delete cascade,
    PRIMARY KEY(ORDER_ID, PRODUCT_ID)
);

INSERT INTO Orders (Order_ID, Date1, Time1, No_of_books, Product_ID)
VALUES 
    ('ORD001', '2024-02-09', '10:00:00', 3, 1),
    ('ORD002', '2024-02-09', '11:30:00', 1, 2),
    ('ORD003', '2024-02-09', '13:45:00', 2, 3),
    ('ORD004', '2024-02-09', '14:15:00', 4, 4),
    ('ORD005', '2024-02-09', '16:20:00', 5, 1);

CREATE TABLE Collects_from (
    Executive_ID int,
    Username varchar(20),
    Order_ID varchar(20),
    FOREIGN KEY (Executive_ID) REFERENCES Delivery_Executive(Executive_ID) on delete cascade,
    FOREIGN KEY (Username) REFERENCES Admin(Username) on delete cascade,
    FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID) on delete cascade,
    Date_of_collection date NOT NULL,
    Time_of_collection time NOT NULL,
    PRIMARY KEY(Executive_ID, Username, Order_ID)
);

INSERT INTO Collects_from (Executive_ID, Username, Order_ID, Date_of_collection, Time_of_collection)
VALUES
(1, 'admin1', 'ORD001', '2024-02-12', '09:00:00'),
(2, 'admin2', 'ORD002', '2024-02-12', '10:30:00'),
(3, 'admin3', 'ORD003', '2024-02-12', '11:45:00'),
(4, 'admin4', 'ORD004', '2024-02-12', '13:15:00'),
(5, 'admin5', 'ORD005', '2024-02-12', '15:00:00');




CREATE TABLE Delivers (
    Executive_ID int,
    Customer_ID varchar(20),
    Order_ID varchar(20),
    Date_of_delivery date NOT NULL,
    Time_of_delivery time NOT NULL,
    Delivery_Status binary, -- Added attribute for delivery status
    FOREIGN KEY (Executive_ID) REFERENCES Delivery_Executive(Executive_ID) on delete cascade,
    FOREIGN KEY (Customer_ID) REFERENCES Users(Customer_ID) on delete cascade,
    FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID) on delete cascade,
    CONSTRAINT chk_delivery_status CHECK (Delivery_Status IN (0,1)),
    PRIMARY KEY (Executive_ID,Customer_ID, Order_ID)
);

INSERT INTO Delivers (Executive_ID, Customer_ID, Order_ID, Date_of_delivery, Time_of_delivery, Delivery_Status)
VALUES
(1, 'CUS001', 'ORD001', '2024-02-12', '09:00:00', 1), 
(2, 'CUS002', 'ORD002',  '2024-02-12', '10:30:00', 0), 
(3, 'CUS003', 'ORD003', '2024-02-12', '11:45:00', 1), 
(4, 'CUS004', 'ORD004', '2024-02-12', '13:15:00', 1), 
(5, 'CUS005', 'ORD005', '2024-02-12', '15:00:00', 0); 

CREATE TABLE ORDER_DETAILS (
    Executive_ID int,
    Customer_ID varchar(20),
    Order_ID varchar(20),
    Quantity integer NOT NULL,
    Total_Transaction_Amount decimal(10,2) NOT NULL,
    FOREIGN KEY (Executive_ID) REFERENCES Delivery_Executive(Executive_ID) on delete cascade,
    FOREIGN KEY (Customer_ID) REFERENCES Users(Customer_ID) on delete cascade,
    FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID) on delete cascade,
    PRIMARY KEY (Executive_ID, Customer_ID, Order_ID)
);


INSERT INTO ORDER_DETAILS (Executive_ID, Customer_ID, Order_ID, Quantity, Total_Transaction_Amount)
VALUES
(1, 'CUS001', 'ORD001', 3, 75.00), 
(2, 'CUS002', 'ORD002', 1, 20.00), 
(3, 'CUS003', 'ORD003', 2, 60.00), 
(4, 'CUS004', 'ORD004', 4, 72.00), 
(5, 'CUS005', 'ORD005', 5, 110.00); 

CREATE TABLE Payments (
    Payment_ID varchar(20) PRIMARY KEY NOT NULL UNIQUE,
    Amount decimal(10,2) NOT NULL,
    Order_ID varchar(20) NOT NULL,
    Mode_of_Payment varchar(20) NOT NULL,
    FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID) on delete cascade
);

INSERT INTO Payments (Payment_ID, Amount, Order_ID, Mode_of_Payment)
VALUES 
    ('PAY001', 50.00, 'ORD001', 'Credit Card'),
    ('PAY002', 30.00, 'ORD002', 'PayPal'),
    ('PAY003', 40.00, 'ORD003', 'Cash'),
    ('PAY004', 60.00, 'ORD004', 'Debit Card'),
    ('PAY005', 70.00, 'ORD005', 'Credit Card');

CREATE TABLE Makes (
    Customer_ID varchar(20),
    Payment_ID varchar(20),
    FOREIGN KEY (Customer_ID) REFERENCES Users(Customer_ID) on delete cascade,
    FOREIGN KEY (Payment_ID) REFERENCES Payments(Payment_ID) on delete cascade,
    PRIMARY KEY (Customer_ID,Payment_ID)
);

INSERT INTO Makes (Customer_ID, Payment_ID)
VALUES
('CUS001', 'PAY001'), 
('CUS002', 'PAY002'), 
('CUS003', 'PAY003'), 
('CUS004', 'PAY004'), 
('CUS005', 'PAY005'); 

CREATE TABLE Admin_Notifications(
	Notification_ID INT AUTO_INCREMENT PRIMARY KEY,
    Message varchar(255),
    Notification_date date NOT NULL
);


	
CREATE INDEX idx_vendor_contact_number ON Vendor (Contact_number);
CREATE INDEX idx_vendor_zipcode ON Vendor (Zipcode);
CREATE INDEX idx_product_vendor_id ON Product (Vendor_ID);
CREATE INDEX idx_product_username ON Product (Username);
CREATE INDEX idx_delivery_executive_contact_number ON Delivery_Executive (Contact_number);
CREATE INDEX idx_delivery_executive_zipcode ON Delivery_Executive (Zipcode);
CREATE INDEX idx_users_contact_number ON Users (Contact_number);
CREATE INDEX idx_users_zipcode ON Users (Zipcode);
CREATE INDEX idx_collects_from_order_id ON Collects_from (Order_ID);
CREATE INDEX idx_purchases_from_vendor_Inventory_id ON Purchases_from (vendor_Inventory_ID);
CREATE INDEX idx_delivers_customer_id ON Delivers (Customer_ID);
CREATE INDEX idx_order_details_customer_id ON ORDER_DETAILS (Customer_ID);
CREATE INDEX idx_payments_order_id ON Payments (Order_ID);
CREATE INDEX idx_makes_customer_id ON Makes (Customer_ID);