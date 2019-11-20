insert into persons values ("Evan", "Timms", "01-02-1998", "Edmonton", "10531 90st SW", "4039936409");
insert into persons values ("Officer", "Jordan", "01-02-1988", "Calgary", "10531 90st SW", "4031234567");
insert into persons values ("Sally", "Timms", "01-02-1998", "Calgary", "9th St SW", "5871238121");

insert into users values ("1504825", "helloworld", "a", "Evan", "Timms", "Edmonton");
insert into users values ("1234567", "helloworld", "o", "Officer", "Jordan", "Edmonton");

insert into vehicles values ("CD43H", "Mazda", "6", 2004, "Red");
insert into vehicles values ("6DGB1", "Porsche", "911", 2015, "Yellow");

insert into registrations values (1234, "2019-01-01", "2019-11-30", "TH34B", "CD43H", "Evan", "Timms");
insert into registrations values (854, "2019-01-01", "2020-01-01", "FHBA2", "6DGB1", "Evan", "Timms");

-- Records of persons
INSERT INTO "persons" VALUES ('Alex', 'Fox', '1995-06-18', 'Montreal', '10234 91 Ave', '780-123-4387');
INSERT INTO "persons" VALUES ('Jane', 'Watch', '1981-11-12', 'Edmonton', '19865 56Ave', '654-123-4789');
INSERT INTO "persons" VALUES ('John', 'Doe', '2000-12-04', 'Edmonton', '3451 129 Ave', '765-128-9123');
INSERT INTO "persons" VALUES ('Roger', 'Peng', '1991-09-04', 'Toronto', '6543 65Ave', '780-175-9875');
INSERT INTO "persons" VALUES ('Matt', 'Smith', '1994-02-17', 'Edmonton', '7654 23 AVe', '587-126-6545');
INSERT INTO "persons" VALUES ('Arash', 'Noruzi', '1991-06-23', 'Calgary', '3451 129 Ave', NULL);
INSERT INTO "persons" VALUES ('Jian', 'Jin', '2000-02-12', 'Edmonton', '1224 14Ave', '129-543-3666');
INSERT INTO "persons" VALUES ('Farnaz', 'Darabi', '1995-05-18', NULL, NULL, NULL);
INSERT INTO "persons" VALUES ('Mina', 'Noruzi', '2016-12-02', 'Edmonton', '3451 129 Ave', NULL);
INSERT INTO "persons" VALUES ('Susan', 'Wayne', '1992-03-12', NULL, NULL, NULL);
INSERT INTO "persons" VALUES ('Jian', 'Lee', '1991-08-12', NULL, NULL, NULL);
INSERT INTO "persons" VALUES ('Tara', 'Jin', '2001-11-30', NULL, NULL, NULL);

-- Records of births
INSERT INTO "births" VALUES (1, 'Jian', 'Jin', '2002-12-20', 'Edmonton', 'm', 'Alex', 'Fox', 'John', 'Doe');
INSERT INTO "births" VALUES (2, 'Mina', 'Noruzi', '2017-01-01', 'Edmonton', 'f', 'Arash', 'Noruzi', 'Farnaz', 'Darabi');

-- Records of marriages
INSERT INTO "marriages" VALUES (1, '2015-01-29', 'Edmonton', 'Arash', 'Noruzi', 'Farnaz', 'Darabi');
INSERT INTO "marriages" VALUES (2, '2013-12-11', 'Calgary', 'John', 'Doe', 'Jane', 'Watch');

-- Records of vehicles
INSERT INTO "vehicles" VALUES (123, 'Toyota', 'Raw 4', 2017, 'Black');
INSERT INTO "vehicles" VALUES (124, 'Honda', 'Civic', 2013, 'Red');
INSERT INTO "vehicles" VALUES (125, 'Ford', 'Fiesta', 2018, 'White');
INSERT INTO "vehicles" VALUES (126, 'Audi', 'Q4', 2016, NULL);
INSERT INTO "vehicles" VALUES (127, 'Toyota', 'Camry', 2017, 'Blue');
INSERT INTO "vehicles" VALUES (128, 'Lexus', 'NX300', 2018, 'Silver');
INSERT INTO "vehicles" VALUES (129, 'Kia', 'Optima', 2012, 'Black');
INSERT INTO "vehicles" VALUES (130, 'Toyota', 'Camry', 2011, 'Blue');
INSERT INTO "vehicles" VALUES (131, 'Toyota', 'Raw 4', 2014, 'Black');
INSERT INTO "vehicles" VALUES (132, 'Toyota', 'Crown', 1996, 'Red');

-- Records of registrations
INSERT INTO "registrations" VALUES (1, '2017-02-03', '2020-02-03', 'A4R3E', 124, 'Jane', 'Watch');
INSERT INTO "registrations" VALUES (2, '2018-11-01', '2019-11-01', 'G76HT', 126, 'Farnaz', 'Darabi');
INSERT INTO "registrations" VALUES (3, '2017-11-29', '2021-11-29', 'U5RFC', 127, 'Roger', 'Peng');
INSERT INTO "registrations" VALUES (4, '2019-01-02', '2020-01-02', 'ABN76', 123, 'Jian', 'Jin');
INSERT INTO "registrations" VALUES (5, '2012-02-17', '2017-02-17', 'ASV6R', 125, 'Jian', 'Jin');
INSERT INTO "registrations" VALUES (6, '2018-05-13', '2020-05-13', 'GF54M', 128, 'Alex', 'Fox');
INSERT INTO "registrations" VALUES (7, '2015-06-21', '2019-06-21', 'BGG65', 129, 'Farnaz', 'Darabi');
INSERT INTO "registrations" VALUES (8, '2019-11-01', '2021-05-12', 'BGG65', 129, 'Jane', 'Watch');
INSERT INTO "registrations" VALUES (9, '2019-08-12', '2020-12-01', 'GFV6R', 130, 'Alex', 'Fox');
INSERT INTO "registrations" VALUES (10, '2019-11-01', '2020-11-01', 'FD543', 131, 'Roger', 'Peng');
INSERT INTO "registrations" VALUES (11, '2019-05-18', '2021-01-01', 'HB65C', 132, 'Susan', 'Wayne');

-- Records of tickets
INSERT INTO "tickets" VALUES (1, 1, 200, 'Speeding', '2019-10-20');
INSERT INTO "tickets" VALUES (2, 2, 120, 'Parking', '2019-08-11');
INSERT INTO "tickets" VALUES (3, 1, 300, 'Speeding', '2019-11-01');
INSERT INTO "tickets" VALUES (4, 3, 100, 'Red Light', '2019-06-30');
INSERT INTO "tickets" VALUES (5, 4, 100, 'Speeding', '2019-01-08');
INSERT INTO "tickets" VALUES (6, 4, 80, 'Parking', '2018-09-12');
INSERT INTO "tickets" VALUES (7, 4, 90, 'Speeding', '2017-10-12');
INSERT INTO "tickets" VALUES (8, 4, 120, 'Red Light', '2019-11-01');
INSERT INTO "tickets" VALUES (9, 4, 130, 'Speeding', '2018-02-13');
INSERT INTO "tickets" VALUES (10, 4, 250, 'Speeding', '2019-03-19');
INSERT INTO "tickets" VALUES (11, 5, 100, 'Parking', '2016-07-18');

-- Records of demeritNotices
INSERT INTO "demeritNotices" VALUES ('2019-10-22', 'Jian', 'Jin', 10, NULL);
INSERT INTO "demeritNotices" VALUES ('2018-12-28', 'Jian', 'Jin', 15, NULL);
INSERT INTO "demeritNotices" VALUES ('2011-09-12', 'Jian', 'Jin', 20, NULL);
INSERT INTO "demeritNotices" VALUES ('2018-11-29', 'Roger', 'Peng', 11, NULL);
INSERT INTO "demeritNotices" VALUES ('2019-10-15', 'Farnaz', 'Darabi', 20, NULL);
INSERT INTO "demeritNotices" VALUES ('2019-03-24', 'Jian', 'Lee', 11, NULL);
INSERT INTO "demeritNotices" VALUES ('2018-12-28', 'Tara', 'Jin', 19, NULL);

-- Records of payments
INSERT INTO "payments" VALUES (2, '2019-11-02', 80);
INSERT INTO "payments" VALUES (1, '2019-10-30', 70);

-- Records of users
INSERT INTO "users" VALUES (1, 'pass123', 'o', 'John', 'Doe', 'Edmonton');
INSERT INTO "users" VALUES (2, 'pass234', 'a', 'Roger', 'Peng', 'Calgary');
