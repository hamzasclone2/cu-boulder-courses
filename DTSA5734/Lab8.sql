-- 3
drop table if exists items;

create table items
(
    itemID integer NOT NULL,
    itemcode varchar(5) NULL,
    itemname varchar(40) NOT NULL default '',
    quantity integer NOT NULL default 0,
    price real NOT NULL default 0
);

-- 4
insert into items 
(select productid,
        concat(supplierid, categoryid, discontinued),
        productname,
        unitsinstock,
        unitprice
        from "alanparadise/nw"."products");