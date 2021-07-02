CREATE TABLE customers (
	customerid BIGINT primary key not null,
	firstname TEXT, 
	surname TEXT
);
INSERT INTO customers (customerid, firstname, surname) VALUES (1, 'Andrew', 'Chisholm');

CREATE TABLE slots (
	slotid BIGINT primary key not null, 
	date DATETIME, 
	maximum_available BIGINT
);
INSERT INTO slots (slotid, date, maximum_available) VALUES (1, '2021-10-01 12:00:00.000000', 20), (2, '2021-10-01 18:00:00.000000', 20), (3, '2021-10-01 20:00:00.000000', 20), (4, '2021-10-02 12:00:00.000000', 20), (5, '2021-10-02 18:00:00.000000', 20), (6, '2021-10-02 20:00:00.000000', 20);

CREATE TABLE bookings (
	bookingid BIGINT primary key not null, 
	customerid BIGINT, 
	slotid BIGINT, 
	number BIGINT,
    constraint customerid_fk foreign key (customerid) references customers(customerid),
    constraint slotid_fk foreign key (slotid) references slots(slotid)
);
INSERT INTO bookings (bookingid, customerid, slotid, number) VALUES (1, 1, 1, 4);

CREATE TABLE administrators (
    username TEXT,
    password TEXT
);
INSERT INTO administrators (username, password) VALUES ('andrew', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8')
