-- 2.1
select orderid, to_char(sum(unitprice * quantity), '999,999.99') as "Total Value"
from "alanparadise/nw"."orderdetails"
group by orderid
order by 2 desc limit 5;

/* 

I originally had the following for 2.1:

select orderid, to_char((unitprice * quantity), '999,999.99') as "Total Value"
from "alanparadise/nw"."orderdetails"
order by 2 desc limit 5;

But this is incorrect because there are multiple rows with the same orderid,
so you need to group them

*/


-- 2.2
select count(*) as "Total Inventory"
from "alanparadise/nw"."products"
where unitsinstock > 0;

-- 2.3
select count(*) as "Out of Stock"
from "alanparadise/nw"."products"
where unitsinstock = 0;

-- 2.4
select supplierid, count(*) as "Total Products"
from "alanparadise/nw"."products"
group by supplierid
order by 2 limit 3;

-- 2.5 
select employeeid, count(*) as "Total Orders"
from "alanparadise/nw"."orders"
group by employeeid
having count(*) > 100;