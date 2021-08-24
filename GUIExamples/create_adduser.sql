CREATE TABLE users (
	username TEXT unique, 
	password TEXT,
    firstname TEXT,
    surname TEXT,
    email TEXT,
    primary key ("username")
);

CREATE TABLE entries (
    username TEXT,
    entry TEXT,
    timestamp REAL unique,
    constraint username foreign key (username) references users(username) on delete cascade
)