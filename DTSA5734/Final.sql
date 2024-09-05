/* 

List employee name (as FirstName Lastname), city, and country for
all employees who work in the US

*/

select concat(firstname, ' ', lastname) as Name, o.city, o.country
from "alanparadise/cm"."employees" e join
     "alanparadise/cm"."offices" o
     on e.officecode = o.officecode
where o.country = 'USA';

/*

List productline, total quantity per product line, and total value 
per product line (quantity * msrp) for each product line and
order the list by descending total value

*/

select productline, sum(quantityinstock) as "Total Quantity",
     to_char(sum(quantityinstock * msrp), '999,999,999.99') 
     as "Total Value"
from "alanparadise/cm"."products"
group by productline
order by 3 desc;

/*

List ordernumber, orderdate, shippeddate, and number of days 
between the two dates for the order with the most amount of days
between the order date and the shipped date

*/

select ordernumber, orderdate, shippeddate,
     to_date(shippeddate,'YYYY-MM-DD') - 
     to_date(orderdate, 'YYYY-MM-DD') as "Days Between"
from "alanparadise/cm"."orders"
where shippeddate is not null
order by 4 desc limit 1;
