/*
Tables to create:

Reviews:
    - 3 Foriegn keys point to members, rides (nullable)
    - rid is p.k
    - rdate, rtext,rscore are attributes
Cars:
    - cno is p.k
    - make, model, year, seats, gdate are attributes
    - 1 foriegn key for registered driver
---- EVAN ----
Rides:
    - rno is p.k
    - price, rdate, seats, lugDesc
    - foriegn key is driver, car, location src, location dst
Bookings:
    - bno is p.k
    - 4 foriegn keys, 2 for locations, 1 for ride, 1 for memember
    - seat, costs as attributes
--- VANIKA --- 
Locations:
    - lcode is p.k
    - address, prov, city are attr
Members:
    - email is p.k
    - name, phone are attributes
--- JORDAN ---
Requests: (NOT SURE YET)
    - amount, qdate are attributes
    - p.k is location lcode + dst lcode + memember email
*/

CREATE TABLE locations (
	lcode INT NOT NULL,
	address VARCHAR(30),
	province VARCHAR(30),
	city VARCHAR(30),
	PRIMARY KEY(lcode)
)

CREATE TABLE members (
	email VARCHAR(30) NOT NULL,
	name VARCHAR(30),
	phone VARCHAR(30),
	PRIMARY KEY(email)
)

CREATE TABLE reviews(
    rid INT NOT NULL,
    rdate DATETIME,
    rtext VARCHAR(1000),
    rscore INT,
    reviewer VARCHAR(30) NOT NULL,
    reviewee VARCHAR(30) NOT NULL,
    ride_number VARCHAR(30),
    PRIMARY KEY(rid),
    FOREIGN KEY (reviewer) REFERENCES members,
    FOREIGN KEY (reviewee) REFERENCES members,
    FOREIGN KEY (ride_number) REFERENCES rides
)

CREATE TABLE cars(
    cno INT NOT NULL,
    make VARCHAR(10),
    model VARCHAR(15),
    model_year DATETIME,
    seats INT,
    gdate DATETIME,
    registered_driver VARCHAR(30) NOT NULL,
    PRIMARY KEY (cno),
    FOREIGN KEY (registered_driver) REFERENCES members ON DELETE CASCADE
)

CREATE TABLE rides(
    rno INT NOT NULL,
    price DECIMAL(19,4),
    rdate DATETIME,
    seats INT,
    lugDesc VARCHAR(1000),
    associated_with INT,
    offered_by VARCHAR(30) NOT NULL,
    ride_src VARCHAR(30) NOT NULL,
    ride_dst VARCHAR(30) NOT NULL,
    enroute_location VARCHAR(30),
    PRIMARY KEY(rno),
    FOREIGN KEY (associated_with) REFERENCES cars,
    FOREIGN KEY (offered_by) REFERENCES members,
    FOREIGN KEY(ride_src) REFERENCES locations,
    FOREIGN KEY(ride_dst) REFERENCES locations,
    FOREIGN KEY(enroute_location) REFERENCES locations ON DELETE CASCADE
)

CREATE TABLE bookings(
    bno INT NOT NULL,
    seats INT,
    cost DECIMAL(19,4),
    for_ride INT NOT NULL,
    reserved_for VARCHAR(30) NOT NULL,
    drop_off VARCHAR(30),
    pickup VARCHAR(30),
    PRIMARY KEY(bno),
    FOREIGN KEY (for_ride) REFERENCES rides,
    FOREIGN KEY (reserved_for) REFERENCES members,
    FOREIGN KEY(drop_off) REFERENCES locations,
    FOREIGN KEY(pickup) REFERENCES locations
)

CREATE TABLE requests (
    amount INT,
    qdate DATETIME,
    dst_code VARCHAR(30),
    lc_code VARCHAR(30),
    request_email VARCHAR(30) NOT NULL,
    FOREIGN KEY(dst_code) REFERENCES locations,
    FOREIGN KEY(lc_code) REFERENCES locations,
    FOREIGN KEY(request_email) REFERENCES members,
    PRIMARY KEY (dst_code, lc_code, request_email)
)


/* Nothing identifies drivers and their licNo. 
Should we have a separate table for drivers? Or is there another way to map it? */  