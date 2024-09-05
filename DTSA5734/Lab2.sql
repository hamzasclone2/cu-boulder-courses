-- 2.1
select customerid, companyname, country
  from "alanparadise/nw"."customers"
 where country != 'USA';

-- 2.2
select productname, unitprice, unitsinstock,
       unitsinstock * unitprice as "Total Value"
  from "alanparadise/nw"."products"
 where unitsinstock * unitprice > 1000;

 -- 2.3
select productid, productname, quantityperunit
  from "alanparadise/nw"."products"
 where quantityperunit like '%bottles%';

-- 2.4
select productid, productname, unitprice
  from "alanparadise/nw"."products"
 where categoryid in (1, 3, 5, 7, 9);

-- 2.5
select orderid, customerid, shippeddate
  from "alanparadise/nw"."orders"
 where shipcountry = 'Canada' and
       shippeddate between '1996-12' and '1997-01'