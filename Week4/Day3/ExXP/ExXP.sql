-- select * from language order by language_id ASC 


-- select title, description, language.name as language from film INNER JOIN language ON film.language_id=language.language_id
-- select title, description, language.name as language from film right JOIN language ON film.language_id=language.language_id
-- select title, description, language.name as language from film left JOIN language ON film.language_id=language.language_id
-- select * from film where language_id = Null


-- create table new_film (
-- id serial primary key,
-- name varchar(50) not null unique
-- );


-- insert into new_film (name)
-- values
-- ('Inception'),
-- ('Bohemian Rhapsody'),
-- ('Nobody');


-- create table customer_review (
-- review_id serial primary key not null,
-- film_id int not null,
-- language_id int not null,
-- title varchar(100) not null,
-- score smallint not null,
-- review_text text not null,
-- last_update date not null,
-- constraint fk_language_id foreign key (language_id) references language(language_id) on delete cascade,
-- constraint fk_film_id foreign key (film_id) references new_film(id) on delete cascade,
-- constraint score check (score <= 10 and score > 0)
-- );


-- insert into customer_review (review_id, film_id, language_id, title, score, review_text, last_update)
-- values
-- (1, 1, 1, 'First review', 9, 'Inception engaged on a mainly intellectually level, but that isnt to say that film didnt pack an emotional impact.', '2023-04-18'),
-- (2, 2, 1, 'Second review', 8, 'In trying to tell Mercury’s queer story through his straight bandmates’ eyes, the new Queen biopic ends up saying almost nothing at all.', '2023-04-17');


-- delete from new_film where name = 'Inception';



-- UPDATE film SET language_id = 6 WHERE title = 'Academy Dinosaur';
-- UPDATE film SET language_id = 1 WHERE title = 'Academy Dinosaur';


-- customer_address_id_fkey


-- select * from rental where return_date is Null


-- select rental.return_date, film.title, film.rental_rate from rental inner join inventory on rental.inventory_id = inventory.inventory_id inner join film on inventory.film_id = film.film_id where rental.return_date is Null  order by rental_rate desc limit 30


-- select film.film_id, film.title, film.description, actor.first_name, actor.last_name from film inner join film_actor on film.film_id = film_actor.film_id inner join actor on actor.actor_id = film_actor.actor_id where film.description like '%Sumo%' and actor.first_name = 'Penelope' and actor.last_name = 'Monroe'

-- select * from film where length < 60 and rating = 'R' and description like '%Documentary%'

-- -- select * from customer where customer.first_name = 'Matthew' 
-- -- customer_id = 323
-- select * from film 
-- inner join inventory on inventory.film_id = film.film_id
-- 	inner join rental on inventory.inventory_id = rental.inventory_id 
-- 		inner join customer on rental.customer_id = customer.customer_id 
-- where customer.customer_id = 323 and film.rental_rate > 4 and rental.return_date between '2005-07-28' and '2005-08-01'

select * from film 
inner join inventory on inventory.film_id = film.film_id
	inner join rental on inventory.inventory_id = rental.inventory_id 
		inner join customer on rental.customer_id = customer.customer_id 
where customer.customer_id = 323 and film.description like '%Boat%' and film.replacement_cost > 18



