-- You are provided a database containing a list of drivers, cars and a schedules 
-- the schedule contains the rides that the drivers have been on, which car was used and when the ride happened 
-- The rides regardless of their schedule date are given ratings of 1-4  based on some metric
-- Each driver can ride in any car, and each car can be driven by any driver. 

.open lq08.db

drop table if exists schedule;
drop table if exists driver;
drop table if exists car;

PRAGMA foreign_keys = ON;

CREATE TABLE driver(
  did   NUMBER,
  dname CHAR(30),
  age   REAL,
  PRIMARY KEY (did)
);
CREATE TABLE car(
  cid   INTEGER,
  make INTEGER,
  color TEXT,
  PRIMARY KEY (cid)
);
CREATE TABLE schedule(
  did  INTEGER,
  cid  INTEGER,
  day  DATE,
  rating  NUMBER,
  FOREIGN KEY (did) REFERENCES driver,
  FOREIGN KEY (cid) REFERENCES car,
  PRIMARY KEY (did,cid,day)
);

-- Populate drivers
INSERT INTO driver VALUES(22,'dustin',45.0);
INSERT INTO driver VALUES(29,'brutus',33.0);
INSERT INTO driver VALUES(31,'lubber',55.0);
INSERT INTO driver VALUES(32,'andy',25.0);
INSERT INTO driver VALUES(58,'rusty',35.0);
INSERT INTO driver VALUES(64,'horatio',35.0);
INSERT INTO driver VALUES(74,'linda',35.0);

-- Populate cars
INSERT INTO car VALUES(101, 'nissan', 'blue');
INSERT INTO car  VALUES(102, 'ford', 'red');
INSERT INTO car VALUES(103, 'daf', 'green');
INSERT INTO car VALUES(104, 'toyota', 'red');
INSERT INTO car VALUES(105, 'Mazda', 'white');

-- Populate schedule
INSERT INTO schedule VALUES(22, 101, '2019-10-10',1);
INSERT INTO schedule VALUES(31, 102, '2019-10-11',2);
INSERT INTO schedule VALUES(22, 103, '2019-06-11',2);
INSERT INTO schedule VALUES(31, 104, '2019-12-11',2);
INSERT INTO schedule VALUES(64, 101, '2019-05-9',3);
INSERT INTO schedule VALUES(22, 102, '2019-08-9',3);
INSERT INTO schedule VALUES(74, 103, '2019-08-9',3);
INSERT INTO schedule VALUES(74, 102, '2019-10-10',4);
INSERT INTO schedule VALUES(22, 103, '2019-08-10',4);
INSERT INTO schedule VALUES(22, 104, '2019-07-10',4);

-- Driver ( did: integer, pname: string,, age: real)
-- Cars( cid: integer, make: string, color: string)
-- schedule(did: integer, cid: integer,  rating: integer,day: date)

