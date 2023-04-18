-- create table person
-- (
-- id serial primary key,
-- name varchar(50) not null
-- );

-- create table passport
-- (
-- passport_id int primary key,
-- constraint fk_person_id foreign key (passport_id) references person(id) on delete cascade
-- );

-- insert into person (name) values
-- ('Ben'), ('John');

-- insert into passport (passport_id)
-- values
-- ((select id from person where name = 'Ben')),
-- ((select id from person where name = 'John'));


-- delete from person where name = 'John';
