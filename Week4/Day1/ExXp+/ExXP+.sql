-- create table students (
-- id serial primary key,
-- last_name varchar(10),
-- first_name varchar(10),	
-- birth_date date
-- ); 


-- insert into students(last_name, first_name, birth_date) 
-- values
-- ('Benichou', 'Marc', '1998-11-02'),
-- ('Cohen', 'Yoan', '2010-12-03'),
-- ('Benichou', 'Lea', '1987-07-27'),
-- ('Dux', 'Amelia', '1996-07-04'),
-- ('Grez', 'David', '2003-06-14'),
-- ('Simpson', 'Omer', '1980-10-03'); 


-- insert into students(last_name, first_name, birth_date) 
-- values
-- ('Boiko', 'Sergei', '1990-12-16'); 


-- select * from students 

-- select * from students where last_name = 'Benichou' and first_name = 'Marc'

-- select * from students where last_name = 'Benichou' or first_name = 'Marc'

-- select * from students where last_name = 'Benichou' or first_name = 'Marc'

-- select * from students where (first_name ~* '[a]') is true

-- select first_name from students where first_name like 'A%';

-- select first_name from students where first_name like '%a';

-- select first_name from students where first_name like '%a_';

-- select * from students where id = 1 or id = 3;


-- XPG

-- select * from students where id >= 1 and id <= 4
-- order by last_name;

-- select * from students
-- order by birth_date
-- DESC LIMIT 1;


-- select * from students where id > 2 limit 3



