-- 3
select * from items;

-- 4
alter table items rename to demo;

-- 5
alter table demo rename column itemcode to itemclass;

-- 6
alter table demo add column iteminfo varchar(5) NULL;

-- 7
update demo set iteminfo = itemclass;

-- 8
select * from demo;