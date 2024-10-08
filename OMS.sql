use OMS;
create table Product(
productid int primary key,
productname varchar(100),
description varchar(500),
price decimal(10,2),
quantityinstock int,
type varchar(50)
);
CREATE TABLE Electronics (
productid int primary key,
brand VARCHAR(255),
warrantyperiod INT,
FOREIGN KEY (productid) REFERENCES Product(productid) ON DELETE CASCADE
);


create table Clothing(
productid int primary key,
size varchar(50),
color varchar(50),
FOREIGN KEY (productid) REFERENCES Product(productid) ON DELETE CASCADE
);

create table Userdetails(
userid int primary key,
username varchar(100) not null unique,
password varchar(200) not null,
role varchar(50) CHECK (role IN ('Admin', 'User'))
);
CREATE TABLE Orders(
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT FOREIGN KEY REFERENCES Userdetails(userid),
    order_date DATETIME DEFAULT GETDATE()
);


CREATE TABLE OrderProduct (
    orderDetailId INT IDENTITY(1,1) PRIMARY KEY,
    order_id INT FOREIGN KEY REFERENCES Orders(order_id),
    product_id INT FOREIGN KEY REFERENCES Product(productid),
    quantity INT NOT NULL
);



select * from Clothing;