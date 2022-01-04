CREATE TABLE customers (
	customerid INTEGER primary key AUTOINCREMENT not null,
	firstname TEXT, 
	surname TEXT
);
--INSERT INTO customers (customerid, firstname, surname) VALUES (1, 'Andrew', 'Chisholm'), (2, "Nicolette", "Dryden");
INSERT INTO customers (firstname, surname) VALUES ('Andrew', 'Chisholm'), ("Nicolette", "Dryden");

CREATE TABLE slots (
	slotid INTEGER primary key AUTOINCREMENT not null, 
	date timestamp, 
	maximum_available INTEGER
);
INSERT INTO slots (date, maximum_available) VALUES ('2021-10-01 12:00:00.000000', 20), ('2021-10-01 18:00:00.000000', 20), ('2021-10-01 20:00:00.000000', 20), ('2021-10-02 12:00:00.000000', 20), ('2021-10-02 18:00:00.000000', 20), ('2021-10-02 20:00:00.000000', 20);

CREATE TABLE bookings (
	bookingid INTEGER primary key AUTOINCREMEnT not null, 
	customerid INTEGER, 
	slotid INTEGER, 
	number INTEGER,
    constraint customerid_fk foreign key (customerid) references customers(customerid),
    constraint slotid_fk foreign key (slotid) references slots(slotid)
);
INSERT INTO bookings (customerid, slotid, number) VALUES (1, 1, 4), (1, 4, 2), (2, 5, 2), (2, 1, 2);

CREATE TABLE administrators (
	administratorid INTEGER primary key AUTOINCREMENT not null,
    username TEXT,
    password TEXT
);
INSERT INTO administrators (username, password) VALUES ('andrew', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8')
