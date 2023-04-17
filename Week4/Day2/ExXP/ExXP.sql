-- select * from customer


-- select concat(first_name, ' ', last_name) as full_name from customer


-- select create_date from customer 
-- group by create_date


-- select * from customer
-- order by first_name DESC


-- select film_id, title, description, release_year, rental_rate from film
-- order by rental_rate ASC


-- Write a query to get the address, and the phone number of all customers living 
-- in the Texas district, these details can be found in the “address” table.


-- select * from customer INNER JOIN address ON customer.address_id=address.address_id WHERE (district='Texas')


-- select * from film where film_id = 15 or film_id = 150


-- select film_id, title, description, length, rental_rate from film where title = 'Ace Goldfinger'


-- select film_id, title, description, length, rental_rate from film where title like 'Ac%'


-- select * from film where rental_rate < 10 
-- order by film_id limit 10

-- select * from film where replacement_cost < 10 
-- order by film_id limit 10


-- select * from film where rental_rate < 10 
-- order by film_id 
-- offset 10
-- fetch first 10 row only

-- select * from film where replacement_cost < 10 
-- order by film_id 
-- offset 10
-- fetch first 10 row only


-- select payment.customer_id, first_name, last_name, amount, payment_date from customer INNER JOIN payment ON customer.customer_id = payment.customer_id
-- order by payment.customer_id ASC


-- select * from film left JOIN inventory ON film.film_id = inventory.film_id where inventory.inventory_id is Null


-- select * from city INNER JOIN country ON city.country_id = country.country_id


-- select customer.customer_id, first_name, last_name, amount, payment_date from payment INNER JOIN customer ON customer.customer_id = payment.customer_id
-- order by staff_id ASC



