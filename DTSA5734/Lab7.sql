-- 2.1
select lastname, firstname, count(orderid) as "Order Total"
from "alanparadise/nw"."employees" E left outer join
     "alanparadise/nw"."orders" O on
     E.employeeid = O.employeeid
group by lastname, firstname
having count(orderid) <= 0;

-- No, there are no employees with no orders

-- 2.2
select companyname, count(orderid) as "Order Total"
from "alanparadise/nw"."customers" C left outer join
     "alanparadise/nw"."orders" O on
     C.customerid = O.customerid
group by companyname
having count(orderid) <= 0;

-- Yes, there are 3 customers with no orders

-- 2.3
select count(distinct O.orderid)
from "alanparadise/nw"."orders" O left outer join
     "alanparadise/nw"."customers" C on
     C.customerid = O.customerid
where C.customerid is NULL;

-- Yes, there are 45 orders with bad customerid's

-- 2.4 
select companyname, count(orderid) as "Order Total"
from "alanparadise/nw"."shippers" S left outer join
     "alanparadise/nw"."orders" O on
     S.shipperid = O.shipvia
group by companyname
having count(orderid) <= 0;

-- No, there are no shippers with no orders