-- Data prepapred by Davood Rafiei, drafiei@ualberta.ca
-- Published on Sept 26, 2019

-- Let's insert some tuples to our tables. This is just an initial set and 
-- we definitly need more data for testing our queries.

insert into persons values ('Michael','Fox','1961-06-09','Edmonton, AB','Manhattan, New York, US', '212-111-1111');
insert into persons values ('Walt', 'Disney', '1901-12-05', 'Chicago, US', 'Los Angeles, US', '213-555-5555');
insert into persons values ('Lillian', 'Bounds', '1899-02-15', 'Spalding, Idaho', 'Los Angeles, US', '213-555-5556');
insert into persons values ('John', 'Truyens', '1907-05-15', 'Flanders, Belgium', 'Beverly Hills, Los Angeles, US', '213-555-5558');
insert into persons values ('Mickey', 'Mouse', '1928-01-05', 'Disneyland', 'Anaheim, US', '714-555-5551');
insert into persons values ('Minnie', 'Mouse', '1928-01-05', 'Disneyland', 'Anaheim, US', '714-555-5552');
-- Let's keep Davood always 21 years old!!
insert into persons values ('Davood','Rafiei',date('now','-21 years'),'Iran','100 Lovely Street,Edmonton,AB', '780-111-2222');

insert into births values (100,'Mickey', 'Mouse', '1928-02-05', 'Anaheim, US', 'M', 'Walt', 'Disney', 'Lillian', 'Bounds');
insert into births values (200,'Minnie', 'Mouse', '1928-02-04', 'Anaheim, US', 'M', 'Walt', 'Disney', 'Lillian', 'Bounds');

-- Partner names can be given in any order (as can be noted)
insert into marriages values (200, '1925-07-13', 'Idaho, US', 'Walt', 'Disney', 'Lillian', 'Bounds');
insert into marriages values (201, '1969-05-03', 'Los Angeles, US', 'Lillian', 'Bounds', 'John', 'Truyens');

insert into vehicles values ('U200', 'Chevrolet', 'Camaro', 1969, 'red');
insert into vehicles values ('U300', 'Mercedes', 'SL 230', 1964, 'black');

insert into registrations values (300, '1964-05-26','1965-05-25', 'DISNEY','U300', 'Walt', 'Disney');
insert into registrations values (302, '1980-01-16','1981-01-15', 'LILLI','U200', 'Lillian', 'Bounds');

insert into tickets values (400,300,4,'speeding','1964-08-20');

insert into demeritNotices values ('1964-08-20', 'Walt', 'Disney', 2, 'Speeding');