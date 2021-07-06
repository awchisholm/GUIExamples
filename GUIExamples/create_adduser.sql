CREATE TABLE users (
	username TEXT, 
	password TEXT
);

CREATE TABLE entries (
    username TEXT,
    entry TEXT,
    timestamp REAL unique
)