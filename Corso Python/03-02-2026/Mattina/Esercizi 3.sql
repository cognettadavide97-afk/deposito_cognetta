select * from film
order by length DESC
LIMIT 10;

#prezzo medio di noleggio (rental_rate) di tutti i film? 
#Rinomina il risultato come "Prezzo_Medio_Noleggio".
SELECT AVG(rental_rate) as Prezzo_Medio_Noleggio from film;
 
 #conta quanti film per ogni durata noleggio
 SELECT * FROM film;
 SELECT rental_duration, count(*) as durata_per_noleggio from film;
 

