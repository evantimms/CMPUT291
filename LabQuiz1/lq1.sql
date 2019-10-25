-- Query 1
select d.did, d.dname, d.age
from driver d
where d.did not in (
    select distinct d2.did
    from driver d2, schedule s
    where d2.did = s.did
);

-- Query 2
select c.cid, c.make, c.color
from car c, schedule s
where c.cid = s.cid
group by c.cid, c.make, c.color
having count(*) > 2;

-- Query 3
select s.rating, avg(d.age)
from schedule s, driver d
where s.did = d.did
and s.rating < date('2019-11-01 00:00:00')
group by s.rating;