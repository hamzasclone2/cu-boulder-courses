-- 3
select * from "MostValuableProducts";

-- 4
drop view if exists "MostValuableProducts";

create view "MostValuableProducts" as
select productname, to_char((unitprice * unitsinstock), '999,999.99') as "Total Current Value",
    case
        when (unitprice * unitsinstock) >= 1000 then 'A'
        when (unitprice * unitsinstock) >= 500 then 'B'
        when (unitprice * unitsinstock) >= 200 then 'C'
        else 'D'
    end "Value Grade"
from "alanparadise/nw"."products"
where (unitprice * unitsinstock) > 0
order by 2 desc;

-- 5
select * from "MostValuableProducts"