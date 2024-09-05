-- 2.1
select city
from "alanparadise/cm"."offices"
order by city;

-- 2.2
select employeenumber, lastname, firstname, extension
from "alanparadise/cm"."employees" e join
     "alanparadise/cm"."offices" o
     on e.officecode = o.officecode
where e.officecode = 4;

-- 2.3
select productcode, productname, productvendor, quantityinstock, productline
from "alanparadise/cm"."products"
where quantityinstock >= 200 and quantityinstock <= 1200;

-- 2.4
select productcode, productname, productvendor, buyprice, msrp
from "alanparadise/cm"."products"
order by 5 asc limit 1;

-- 2.5
select productname, (msrp-buyprice) as "profit"
from "alanparadise/cm"."products"
order by 2 desc limit 1;

-- 2.6
select country, count(*) as "Customers"
from "alanparadise/cm"."Customers"
group by country
having count(*)=2
order by 1 asc;

-- 2.7
select p.productcode, p.productname, count(*) as "OrderCount"
from "alanparadise/cm"."orderdetails" o join
     "alanparadise/cm"."products" p
     on p.productcode = o.productcode
group by p.productcode, p.productname
having count(*)=25;

-- 2.8
select employeenumber, concat(firstname, ' ', lastname) as "name"
from "alanparadise/cm"."employees"
where reportsto = 1002 or reportsto = 1102;

-- 2.9
select employeenumber, concat(firstname, ' ', lastname) as "name"
from "alanparadise/cm"."employees"
where reportsto IS null;

-- 2.10
select productname
from "alanparadise/cm"."products"
where productline = 'Classic Cars' and productname like '195%';

-- 2.11 WRONG

select orderdate, count(*)
from "alanparadise/cm"."orders" o join
     "alanparadise/cm"."orderdetails" od 
     on o.ordernumber = od.ordernumber
where orderdate like '2004%'
group by orderdate
order by 2 desc;

-- 2.12
select firstname, lastname
from "alanparadise/cm"."employees" e left join
     "alanparadise/cm"."Customers" c
     on e.employeenumber = c.salesrepemployeenumber
where jobtitle = 'Sales Rep' and c.salesrepemployeenumber is null;

-- 2.13 
select customername
from "alanparadise/cm"."Customers" c left join
     "alanparadise/cm"."orders" o 
     on c.customernumber = o.customernumber
where country = 'Switzerland' and o.customernumber is null;

-- 2.14
select customername, sum(quantityordered)
from "alanparadise/cm"."orderdetails" od join
     "alanparadise/cm"."orders" o
     on o.ordernumber = od.ordernumber join
     "alanparadise/cm"."Customers" c on
     o.customernumber = c.customernumber
group by customername
having sum(quantityordered) > 1650;

/* ---------------------------------- */

-- 2.2.1

drop table if exists TopCustomers;

create table TopCustomers (
    CustomerNumber integer not null,
    ContactDate date not null,
    OrderTotal real not null
);

-- 2.2.2
insert into TopCustomers
(select c.customernumber, CURRENT_DATE, sum(priceeach * quantityordered)
from "alanparadisecm"."Customers" c join
     "alanparadisecm"."orders" o
     on c.customernumber = o.customernumber join
     "alanparadisecm"."orderdetails" od
     on od.ordernumber = o.ordernumber
group by c.customernumber
having sum(priceeach * quantityordered) > 14000);

-- 2.2.3
select *
from TopCustomers
order by ordertotal desc;

-- 2.2.4
alter table TopCustomers
add column OrderCount integer;

-- 2.2.5
update TopCustomers
set ordercount = random() * 10;

-- 2.2.6
select *
from TopCustomers
order by OrderCount desc;

-- 2.2.7
drop table TopCustomers;
