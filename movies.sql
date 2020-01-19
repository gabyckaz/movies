BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "rents" (
	"id_rent"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"id_user"	INTEGER NOT NULL,
	"id_movie"	INTEGER NOT NULL,
	"return_date"	TEXT,
	"price_penalty"	REAL,
	"status"	INTEGER,
	FOREIGN KEY("id_movie") REFERENCES "movies"("id_movie"),
	FOREIGN KEY("id_user") REFERENCES "users"("id_user")
);
CREATE TABLE IF NOT EXISTS "users" (
	"id_user"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT,
	"role"	TEXT,
	"pass"	TEXT
);
CREATE TABLE IF NOT EXISTS "sales" (
	"id_sale"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"id_user"	INTEGER NOT NULL,
	"id_movie"	INTEGER NOT NULL,
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
INSERT INTO "rents" ("id_rent","id_user","id_movie","return_date","price_penalty","status") VALUES (1,2,21,'2019-01-22',3.5,0);
INSERT INTO "users" ("id_user","name","role","pass") VALUES (1,'jack','admin','pbkdf2:sha256:150000$HGBSb2pq$c6e724e297455f8dc2b488bc22abfef92114d3a498ded9549c537424f43fae8e');
INSERT INTO "users" ("id_user","name","role","pass") VALUES (2,'maria','client','pbkdf2:sha256:150000$PQ9UeHDg$96b86acee6a624f632c13de91b0f6d176a29a7accad604c353f2e639d98abcd4');
INSERT INTO "sales" ("id_sale","id_user","id_movie") VALUES (9,2,2);
INSERT INTO "sales" ("id_sale","id_user","id_movie") VALUES (10,2,3);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (1,'Shrek','Shrek is a 2001 American computer-animated comedy film loosely based on the 1990 fairytale picture book of the same name by William Steig.','https://img.favpng.com/18/16/8/shrek-the-musical-princess-fiona-lord-farquaad-shrek-film-series-png-favpng-mPpYHdacThLntYYJQdX8faf1y.jpg',19,8.5,12.99,0,35);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (2,'Ice Age','Ice Age is an American media franchise centering on a group of mammals surviving the Paleolithic ice age.','https://is5-ssl.mzstatic.com/image/thumb/Video49/v4/33/b3/d0/33b3d0a5-8961-468e-d70a-52df0ef1680d/pr_source.lsr/268x0w.png',4,7.8,10.5,1,14);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (3,'Harry Potter and the Philosopher''s Stone','Its story follows Harry Potter''s first year at Hogwarts School of Witchcraft and Wizardry as he discovers that he is a famous wizard and begins his education.','https://is2-ssl.mzstatic.com/image/thumb/Video128/v4/55/60/fc/5560fcab-339a-1ca5-9193-555c9ff31df1/pr_source.lsr/268x0w.png',11,6.99,13.45,0,26);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (7,'Lemony Snicket''s A Series of Unfortunate Events','Fourteen-year-old inventor Violet Baudelaire, her twelve-year-old bibliophile brother Klaus, and their mordacious baby sister Sunny are orphaned after a mysterious fire destroys their home and kills their parents. ','https://upload.wikimedia.org/wikipedia/en/thumb/c/cb/A_Series_Of_Unfortunate_Events_poster.jpg/220px-A_Series_Of_Unfortunate_Events_poster.jpg',22,13.55,9.99,0,0);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (8,'Parasite','Is a 2019 South Korean black comedy thriller film directed by Bong Joon-ho, who also wrote the film''s story and co-wrote the screenplay with Han Jin-won, follows the members of a poor household scheming to become employees of a much wealthier family by posing as unrelated, highly qualified individuals.','https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Parasite_%282019_film%29.png/220px-Parasite_%282019_film%29.png',30,9.55,10.99,0,0);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (11,'Die Hard','On Christmas Eve, NYPD detective John McClane arrives in Los Angeles, intending to reconcile with his estranged wife, Holly, at the Christmas party of her employer, the Nakatomi Corporation. McClane is driven to the party by Argyle, a limousine driver. While McClane changes clothes, the party is disrupted by the arrival of a German terrorist, Hans Gruber, and his team. The group seizes the tower, disables communication to the outside world, and secures those inside as hostages except for McClane, who slips away, and Argyle, who gets stranded in the garage.','https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Die_hard.jpg/220px-Die_hard.jpg',15,6.58,15.5,0,0);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (12,'The Greatest Showman','Celebrates the birth of show business and tells of a visionary who rose from nothing to create a spectacle that became a worldwide sensation.','https://upload.wikimedia.org/wikipedia/en/1/10/The_Greatest_Showman_poster.png',15,7.68,13.66,0,0);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (13,'Avengers: Endgame',' Endgame is a 2019 American superhero film based on the Marvel Comics superhero team the Avengers, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.','https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg',25,8.55,13.47,1,40);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (14,'Avatar','The film is set in the mid-22nd century when humans are colonizing Pandora, a lush habitable moon of a gas giant in the Alpha Centauri star system, in order to mine the mineral unobtanium, a room-temperature superconductor. The expansion of the mining colony threatens the continued existence of a local tribe of Na''vi – a humanoid species indigenous to Pandora. ','https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg',225,18.55,13.47,0,0);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (15,'Into the Woods',' Inspired by the Grimm Brothers'' fairy tales of "Little Red Riding Hood", "Cinderella", "Jack and the Beanstalk" and "Rapunzel", the film is a fantasy genre centered on a childless couple, who set out to end a curse placed on them by a vengeful witch. Ultimately, the characters are forced to experience the consequences of their actions','https://upload.wikimedia.org/wikipedia/en/thumb/3/34/Into_the_Woods_film_poster.jpg/220px-Into_the_Woods_film_poster.jpg',30,8.51,16.51,0,2);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (20,'Jokered','edJoker provides a possible origin story for the character; set in 1981, it follows Arthur Fleck, a failed stand-up comedian whose descent into insanity and nihilism inspires a violent counter-cultural revolution against the wealthy in a decaying Gotham City.','edhttps://upload.wikimedia.org/wikipedia/en/e/e1/Joker_%282019_film%29_poster.jpg',220,111.8,115.99,1,1);
INSERT INTO "movies" ("id_movie","title","description","image","stock","rent_price","sale_price","availability","popularity") VALUES (21,'Titanic','Titanic is a 1997 American epic romance and disaster film. Incorporating both historical and fictionalized aspects, the film is based on accounts of the sinking of the RMS Titanic','https://upload.wikimedia.org/wikipedia/en/1/19/Titanic_%28Official_Film_Poster%29.png',30,5.99,9.95,1,29);
COMMIT;
