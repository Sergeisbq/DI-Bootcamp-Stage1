-- create table items (
-- id serial primary key,
-- name varchar(50) not null unique,
-- price int
-- );

-- create table product_orders (
-- id serial primary key,
-- quantity int not null,
-- "date" timestamp not null default current_timestamp,
-- product_id int references items(id) on delete no action
-- );

-- insert into items (name, price)
-- values
-- ('TV', 50),
-- ('Duck', 44),
-- ('Radio', 22);


-- insert into product_orders (quantity, product_id)
-- values
-- (1, (select id from items where name = 'TV')),
-- (5, (select id from items where name = 'Duck')),
-- (2, (select id from items where name = 'Radio'));

-- insert into product_orders (quantity, product_id)
-- values
-- (3, (select id from items where name = 'TV'));


-- select name, quantity, price from product_orders
-- join items
-- on
-- product_orders.product_id = items.id
-- where product_orders.id = 1;



-- create or replace function order_price (order_id int)
-- returns int as $$

-- 	declare
-- 		total_sum int;
		
-- 	begin
-- 		total_sum := (select sum(quantity * price) from product_orders
-- 			join items
-- 			on
-- 			product_orders.product_id = items.id
-- 			where product_orders.id = order_id);
-- 		return total_sum;
-- 	end;
	
-- $$ language plpgsql;

select order_price(3);


