-- create table customer (
-- id int primary key,
-- first_name varchar(50) NOT NULL,
-- last_name varchar(50) NOT NULL
-- );


-- create table customer_profile (
-- id int primary key,
-- isLoggedIn bool DEFAULT false, 
-- customer_profile_id int references customer(id) on delete no action
-- );


-- insert into customer (id, first_name, last_name)
-- values
-- (1, 'John', 'Doe'),
-- (2, 'Jerome', 'Lalu'),
-- (3, 'Lea', 'Rive');


-- insert into customer_profile (id, isLoggedIn, customer_profile_id)
-- values
-- (1, True, (select id from customer where first_name = 'John')),
-- (2, False, (select id from customer where first_name = 'Jerome'));


-- select first_name from customer inner join customer_profile on customer_profile.customer_profile_id = customer.id where customer_profile.isLoggedIn is True 

-- select first_name, customer_profile.isLoggedIn from customer left join customer_profile on customer_profile.customer_profile_id = customer.id 

-- select count(*) from customer left join customer_profile on customer_profile.customer_profile_id = customer.id where customer_profile.isLoggedIn is False 




-- create table book (
-- book_id SERIAL PRIMARY KEY,
-- title text NOT NULL,
-- author varchar(50) NOT NULL
-- );


-- insert into book (book_id, title, author)
-- values
-- (1, 'Alice In Wonderland', 'Lewis Carroll'),
-- (2, 'Harry Potter', 'J.K Rowling'),
-- (3, 'To kill a mockingbird', 'Harper Lee');


-- create table student (
-- student_id SERIAL PRIMARY KEY,
-- name varchar(50) NOT NULL UNIQUE,
-- age smallint NOT NULL check (age between 0 and 15)
-- );


-- insert into student (student_id, name, age)
-- values
-- (1, 'John', 12),
-- (2, 'Lera', 11),
-- (3, 'Patrick', 10),
-- (4, 'Bob', 14);


-- create table library (
-- book_fk_id int NOT NULL,
-- student_fk_id int NOT NULL,
-- borrowed_date date NOT NULL,
-- foreign key (book_fk_id) references book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- foreign key (student_fk_id) references student (student_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- primary key (book_fk_id, student_fk_id)
-- );


-- insert into library (book_fk_id, student_fk_id, borrowed_date)
-- values 
-- (
-- (select book_id from book where title ilike 'Alice In Wonderland'), 
-- (select student_id from student where name ilike 'John'),
-- '2022-02-15' 
-- );

-- insert into library (book_fk_id, student_fk_id, borrowed_date)
-- values 
-- (
-- (select book_id from book where title ilike 'To kill a mockingbird'), 
-- (select student_id from student where name ilike 'Bob'),
-- '2021-03-03' 
-- );

-- insert into library (book_fk_id, student_fk_id, borrowed_date)
-- values 
-- (
-- (select book_id from book where title ilike 'Alice In Wonderland'), 
-- (select student_id from student where name ilike 'Lera'),
-- '2021-05-23' 
-- );

-- insert into library (book_fk_id, student_fk_id, borrowed_date)
-- values 
-- (
-- (select book_id from book where title ilike 'Harry Potter'), 
-- (select student_id from student where name ilike 'Bob'),
-- '2021-08-12' 
-- );


-- select * from library

-- select student.name, book.title from library 
-- 	inner join student on library.student_fk_id = student.student_id
-- 		inner join book on library.book_fk_id = book.book_id
-- order by student.name

-- select avg(student.age) from student 
-- 	inner join library on library.student_fk_id = student.student_id
-- 		inner join book on library.book_fk_id = book.book_id
-- where book.title = 'Alice In Wonderland'

-- delete from student where student_id = 1





