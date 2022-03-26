BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Favourite" (
	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"PersonID"	INTEGER,
	"FoodID"	INTEGER,
	FOREIGN KEY("FoodID") REFERENCES "FoodAndBeverage"("ID"),
	FOREIGN KEY("PersonID") REFERENCES "Person"("ID")
);
CREATE TABLE IF NOT EXISTS "FoodAndBeverage" (
	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Food"	TEXT
);
CREATE TABLE IF NOT EXISTS "Person" (
	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"FirstName"	TEXT
);
INSERT INTO "Favourite" VALUES (1,1,1);
INSERT INTO "Favourite" VALUES (3,1,7);
INSERT INTO "Favourite" VALUES (4,17,3);
INSERT INTO "FoodAndBeverage" VALUES (1,'Wine');
INSERT INTO "FoodAndBeverage" VALUES (2,'Beer');
INSERT INTO "FoodAndBeverage" VALUES (3,'Chocolate');
INSERT INTO "FoodAndBeverage" VALUES (4,'Pizza');
INSERT INTO "FoodAndBeverage" VALUES (5,'Cheese On Toast');
INSERT INTO "FoodAndBeverage" VALUES (6,'Fillet Steak');
INSERT INTO "FoodAndBeverage" VALUES (7,'Steak and Kidney Pudding');
INSERT INTO "Person" VALUES (1,'Andrew');
INSERT INTO "Person" VALUES (2,'Jono');
INSERT INTO "Person" VALUES (3,'Josh A');
INSERT INTO "Person" VALUES (4,'Josh T');
INSERT INTO "Person" VALUES (5,'Josh F');
INSERT INTO "Person" VALUES (6,'Josh P');
INSERT INTO "Person" VALUES (7,'George');
INSERT INTO "Person" VALUES (8,'Jono');
INSERT INTO "Person" VALUES (9,'Aksel');
INSERT INTO "Person" VALUES (10,'Crystal');
INSERT INTO "Person" VALUES (11,'Kayleigh');
INSERT INTO "Person" VALUES (12,'Mina');
INSERT INTO "Person" VALUES (13,'Joel');
INSERT INTO "Person" VALUES (14,'Freddie');
INSERT INTO "Person" VALUES (15,'Jack');
INSERT INTO "Person" VALUES (16,'Aidan');
INSERT INTO "Person" VALUES (17,'Nicolette');
INSERT INTO "Person" VALUES (18,'Steve');

COMMIT;
