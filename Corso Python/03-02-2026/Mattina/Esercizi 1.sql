select rental_id, amount from payment
where amount=0.99;


select rental_id, amount from payment
where amount>4;

select * from film
order by length DESC;

select * from film
order by length DESC
LIMIT 10;

SELECT * from film
where title like "%aby%";

select * from film
where length>120 AND rental_rate<10;

select * from film
where length>180 OR length<60;

select * from film
where length between 60 and 90;

select * from film
where rating IN ("G","R");

select distinct rental_rate from film;

select count(*) from film;

select rating, count(*) as totale_film
from film
group by rating;

select * from payment;

select customer_id, SUM(amount) as totale_speso
from payment
group by customer_id;actor