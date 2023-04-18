-- create or replace function full_name(first_name varchar(50), last_name varchar(50))
-- returns varchar(100) as $$
-- 	begin
-- 		return first_name ||' '|| last_name;
-- 	end
-- $$ language plpgsql


-- select * from full_name ('Yossi', 'Eik')

-- select full_name (first_name, last_name) from actors;

select number_oscars, full_name (first_name, last_name) from actors;