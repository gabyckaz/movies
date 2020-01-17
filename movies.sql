BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "sales" (
	"id_sale"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"id_user"	INTEGER NOT NULL,
	"id_movie"	INTEGER NOT NULL,
	FOREIGN KEY("id_user") REFERENCES "users"("id_user")
);
CREATE TABLE IF NOT EXISTS "rents" (
	"id_rent"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"id_user"	INTEGER NOT NULL,
	"id_movie"	INTEGER NOT NULL,
	"return_date"	TEXT,
	"price_penalty"	REAL,
	FOREIGN KEY("id_movie") REFERENCES "movies"("id_movie"),
	FOREIGN KEY("id_user") REFERENCES "users"("id_user")
);
CREATE TABLE IF NOT EXISTS "movies" (
	"id_movie"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"title"	TEXT,
	"description"	TEXT,
	"image"	TEXT,
	"stock"	INTEGER,
	"rent_price"	REAL,
	"sale_price"	REAL,
	"availability"	INTEGER,
	"popularity"	INTEGER
);
CREATE TABLE IF NOT EXISTS "users" (
	"id_user"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"role"	TEXT,
	"name"	TEXT
);
INSERT INTO "sales" ("id_sale","id_user","id_movie") VALUES (1,2,9);
INSERT INTO "sales" ("id_sale","id_user","id_movie") VALUES (2,2,8);
INSERT INTO "sales" ("id_sale","id_user","id_movie") VALUES (3,2,13);
INSERT INTO "rents" ("id_rent","id_user","id_movie","return_date","price_penalty") VALUES (1,2,3,'2019-01-20',3.5);
INSERT INTO "rents" ("id_rent","id_user","id_movie","return_date","price_penalty") VALUES (2,2,2,'2019-01-20',3.5);
INSERT INTO "rents" ("id_rent","id_user","id_movie","return_date","price_penalty") VALUES (3,2,1,'2019-01-20',3.5);
INSERT INTO "rents" ("id_rent","id_user","id_movie","return_date","price_penalty") VALUES (4,2,5,'2019-01-20',3.5);
INSERT INTO "rents" ("id_rent","id_user","id_movie","return_date","price_penalty") VALUES (5,2,8,'2019-01-23',3.5);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (1,'Shrek','Shrek is a 2001 American computer-animated comedy film loosely based on the 1990 fairytale picture book of the same name by William Steig.','https://img.favpng.com/18/16/8/shrek-the-musical-princess-fiona-lord-farquaad-shrek-film-series-png-favpng-mPpYHdacThLntYYJQdX8faf1y.jpg',20,8.5,12.99,0,35);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (2,'Ice Age','Ice Age is an American media franchise centering on a group of mammals surviving the Paleolithic ice age.','https://is5-ssl.mzstatic.com/image/thumb/Video49/v4/33/b3/d0/33b3d0a5-8961-468e-d70a-52df0ef1680d/pr_source.lsr/268x0w.png',5,7.8,10.5,1,14);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (3,'Harry Potter and the Philosopher''s Stone','Its story follows Harry Potter''s first year at Hogwarts School of Witchcraft and Wizardry as he discovers that he is a famous wizard and begins his education.','https://is2-ssl.mzstatic.com/image/thumb/Video128/v4/55/60/fc/5560fcab-339a-1ca5-9193-555c9ff31df1/pr_source.lsr/268x0w.png',13,6.99,13.45,0,26);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (7,'nueva pelicula','descripciooooon','http://imgdfcdf.com',10,8.55,12.54,1,0);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (8,'nueva pelicula','descripciooooon','http://imgdfcdf.com',10,8.55,12.54,1,0);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (9,'','descripciooooon','http://imgdfcdf.com',10,8.55,12.54,1,0);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (10,'b''''','descripciooooon','http://imgdfcdf.com',10,8.55,12.54,1,0);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (11,'','descripciooooon','http://imgdfcdf.com',10,8.55,12.54,1,0);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (12,'','descripciooooon','http://imgdfcdf.com',10,8.55,12.54,1,0);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (13,'Avengers: Endgame',' Endgame is a 2019 American superhero film based on the Marvel Comics superhero team the Avengers, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.','https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg',4,8.55,16.47,1,36);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (14,'q','descripciooooon','http://imgdfcdf.com',10,8.55,12.54,1,0);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (15,'q','descripciooooon','http://imgdfcdf.com',10,8.55,12.54,1,0);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (20,'Jokered','edJoker provides a possible origin story for the character; set in 1981, it follows Arthur Fleck, a failed stand-up comedian whose descent into insanity and nihilism inspires a violent counter-cultural revolution against the wealthy in a decaying Gotham City.','edhttps://upload.wikimedia.org/wikipedia/en/e/e1/Joker_%282019_film%29_poster.jpg',220,111.8,115.99,1,1);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (21,'Titanic','Titanic is a 1997 American epic romance and disaster film. Incorporating both historical and fictionalized aspects, the film is based on accounts of the sinking of the RMS Titanic','https://upload.wikimedia.org/wikipedia/en/1/19/Titanic_%28Official_Film_Poster%29.png',30,5.99,9.95,0,27);
INSERT INTO "users" ("id_user","role","name") VALUES (1,'admin','Jack');
INSERT INTO "users" ("id_user","role","name") VALUES (2,'client','Maria');
COMMIT;
