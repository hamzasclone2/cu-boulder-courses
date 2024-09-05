-- 2.1
select productid, productname, unitprice
from "alanparadise/nw"."products"
where unitprice = (
    select MIN(unitprice)
        from "alanparadise/nw"."products" 
);

-- 2.2
select count(*)
from "alanparadise/nw"."orders"
where customerid NOT in
(select customerid from "alanparadise/nw"."customers")
