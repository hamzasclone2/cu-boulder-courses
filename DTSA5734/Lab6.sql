-- 2.1
select OD.orderid, to_char(sum(unitprice * quantity), '999,999.99') as "Total Value"
from "alanparadise/nw"."orders" O,
     "alanparadise/nw"."orderdetails" OD
where shipcountry = 'France' and O.orderid = OD.orderid
group by OD.orderid, OD.unitprice, OD.quantity
order by 2 desc;


-- 2.2
select companyname, productname
from "alanparadise/nw"."suppliers" S,
     "alanparadise/nw"."products" P
where country = 'Japan' and S.supplierid = P.supplierid;

-- 2.3
select lastname, firstname, to_char(sum(unitprice * quantity), '999,999.99') as "Total Value"
from "alanparadise/nw"."employees" E JOIN
     "alanparadise/nw"."orders" O
    on E.employeeid = O.employeeid JOIN
    "alanparadise/nw"."orderdetails" OD
    on O.orderid = OD.orderid
group by lastname, firstname
having sum(unitprice * quantity) < 100000
order by 3 desc;