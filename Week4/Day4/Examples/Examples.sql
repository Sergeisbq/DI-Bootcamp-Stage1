-- select column
-- select first_name from actor order by first_name desc;

-- select + order by
-- select first_name from actor order by first_name desc;

-- select + condition
-- select first_name from actor where first_name ilike 'b%';

-- select + condition + order by
-- select first_name, last_name from actor where first_name ilike 'b%' order by last_name desc;

-- select + aggregate function + group by
-- options: maz, min, avg, sum, count
-- select count(first_name), sum(actor_id) from actor where first_name ilike 'b%'

-- select column_table1, column_table2 + join + on/condition
-- inner join
-- select city, country from city as ci
-- 	inner join country as co
-- 		on ci.country_id = co.country_id
		
-- left join
-- select title, name from film as f
-- 	left join language as l
-- 		on f.language_id = l.language_id
		
-- right join
-- select title, name from film as f
-- 	right join language as l
-- 		on f.language_id = l.language_id


-- select + aggregate function + group by
select country, count(city) 
from city as ci
	inner join country as co
		on ci.country_id = co.country_id
group by country