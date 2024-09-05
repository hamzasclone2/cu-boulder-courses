-- 2.1 
select employeeid, concat(firstname, ' ', lastname) as "Employee", age(hiredate, birthdate) as "Hire Age"
from "alanparadise/nw"."employees";

-- 2.2
select age(current_date, to_date('19960718', 'YYYYMMDD'));

-- 2.3
select customerid, companyname, country
from "alanparadise/nw"."customers"
where region is NULL;