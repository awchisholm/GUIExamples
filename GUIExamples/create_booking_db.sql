CREATE TABLE users (
	firstname TEXT, 
	surname TEXT, 
	username TEXT primary key not null
);
INSERT INTO users (firstname, surname, username) VALUES ('Andrew', 'Chisholm', 'andrew');

CREATE TABLE slots (
	slotid BIGINT primary key not null, 
	date DATETIME, 
	maximum_available BIGINT
);
INSERT INTO slots (slotid, date, maximum_available) VALUES (1, '2021-10-01 12:00:00.000000', 20), (2, '2021-10-01 18:00:00.000000', 20), (3, '2021-10-01 20:00:00.000000', 20), (4, '2021-10-02 12:00:00.000000', 20), (5, '2021-10-02 18:00:00.000000', 20), (6, '2021-10-02 20:00:00.000000', 20);

CREATE TABLE bookings (
	bookingid BIGINT primary key not null, 
	username TEXT, 
	slotid BIGINT, 
	number BIGINT,
    constraint username_fk foreign key (username) references users(username),
    constraint slotid_fk foreign key (slotid) references slots(slotid)
);
INSERT INTO bookings (bookingid, username, slotid, number) VALUES (1, 'andrew', 1, 4);

CREATE TABLE userlogin (
    username TEXT,
    password TEXT,
    constraint username_fk foreign key (username) references users(username)
);
INSERT INTO userlogin (username, password) VALUES ('andrew', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8')
