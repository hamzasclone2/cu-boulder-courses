-- 3
create view "MostValuableProducts" as
select productname, to_char((unitprice * unitsinstock), '999,999.99') as "Total Current Value"
from "alanparadise/nw"."products"
where (unitprice * unitsinstock) > 0
order by 2 desc;

-- 4
select * from "MostValuableProducts";