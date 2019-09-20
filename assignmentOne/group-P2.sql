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

CREATE TABLE members(
    phone CHAR(9),
    name VARCHAR(30),
    email VARCHAR(30),
    PRIMARY KEY(email)
)