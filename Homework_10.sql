-- IMARA PAIZ
--
-- 1a. Display the first and last names of all actors from the table actor.
--
use sakila;
select first_name, last_name 
from actor;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. 
-- Name the column Actor Name.
select concat(first_name,' ',last_name) as Actor_Name
from actor;

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." 
-- What is one query would you use to obtain this information?
select actor_id, first_name, last_name
from actor 
where first_name = 'Joe'; 

-- 2b. Find all actors whose last name contain the letters GEN:
select actor_id, first_name, last_name
from actor
where last_name like '%GEN%';

-- 2c. Find all actors whose last names contain the letters LI. 
-- This time, order the rows by last name and first name, in that order:
select actor_id, first_name, last_name
from actor
where last_name like '%LI%'
order by last_name, first_name;

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
select country_id, country
from country
where country in ('Afghanistan', 'Bangladesh', 'China');

-- 3a. Add a middle_name column to the table actor. Position it between first_name and last_name. 
-- Hint: you will need to specify the data type.
alter table actor
add column middle_name varchar(30) after first_name;

-- 3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.
alter table actor
modify column middle_name blob;

-- 3c. Now delete the middle_name column.
alter table actor
drop column middle_name;

-- 4a. List the last names of actors, as well as how many actors have that last name.
select last_name, count(*)
from actor
group by last_name;

-- 4b. List last names of actors and the number of actors who have that last name, 
-- but only for names that are shared by at least two actors
select last_name, count(*) as count_share
from actor
group by last_name 
having count_share >=2;

-- 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, 
-- the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
set sql_safe_updates = 0;
update actor 
set first_name = 'HARPO'
where actor_id = '172';
set sql_safe_updates = 1;

select * from actor where last_name like '%WILL%';

-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! 
-- In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO. 
-- Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. 
-- BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! 
-- (Hint: update the record using a unique identifier.)
set sql_safe_updates = 0;
update actor 
set first_name = 
	case when (first_name = 'HARPO') 
		then 'GROUCHO' 
		else 'MUCHO GROUCHO' 
	end
where actor_id = '172' and first_name = 'HARPO';
set sql_safe_updates = 1;

-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
use sakila;
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE table_name = 'address';

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. 
-- Use the tables staff and address:
select f.first_name, f.last_name, a.address
from staff f inner join address a on f.address_id = a.address_id;

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
select s.staff_id, sum(p.amount) as amount_rung
from staff s join payment p on s.staff_id = p.staff_id
where p.payment_date like '2005-08%'
group by s.staff_id;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
select f.film_id, f.title, count(*) as num_actors
from film f inner join film_actor a on a.film_id = f.film_id
group by f.film_id;

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
select i.film_id, count(*)
from inventory i inner join film f on i.film_id = f.film_id
where f.title = 'Hunchback Impossible'
group by i.film_id;

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. 
-- List the customers alphabetically by last name:
select c.first_name, c.last_name, sum(amount) total_paid
from payment p join customer c on c.customer_id = p.customer_id
group by c.first_name, c.last_name
order by last_name;

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
-- As an unintended consequence, films starting with the letters K and Q have also soared in popularity. 
-- Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
select f.title
from film f 
where (f.title like ('K%') or f.title like ('Q%'))
 and f.language_id = (select l.language_id
						from language l 
						where l.name = 'English');


-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
use sakila;
select first_name, last_name 
from actor
where actor_id in (select actor_id
					from film_actor
                    where film_id = (select film_id
										from film
                                        where title = 'Alone Trip'
                                        )
					);
                    
-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses 
-- of all Canadian customers. Use joins to retrieve this information.
select c.first_name, c.last_name, c.email
from customer c
	inner join address a on a.address_id = c.address_id
    inner join city i on i.city_id = a.city_id
    inner join country n on n.country_id = i.country_id
    and n.country = 'Canada';
    
-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
-- Identify all movies categorized as famiy films.
select f.film_id, f.title
from film f 
	inner join film_category l on l.film_id = f.film_id
    inner join category c on c.category_id = l.category_id
			and c.name = 'Family';
            
-- 7e. Display the most frequently rented movies in descending order.
select r.inventory_id, r.rental_times, f.title
from (
	select inventory_id, count(*) as rental_times
	from rental
	group by inventory_id
	having rental_times > 1) r
	inner join inventory i on i.inventory_id = r.inventory_id
	inner join film f on f.film_id = i.film_id
order by rental_times desc;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
select s.store_id, sum(p.amount)
from payment p 
	inner join rental r on p.rental_id = r.rental_id
    inner join inventory i on i.inventory_id = r.inventory_id
    inner join store s on s.store_id = i.store_id
group by s.store_id;
    
-- 7g. Write a query to display for each store its store ID, city, and country.
select s.store_id, c.city, t.country
from store s
	join address a on s.address_id = a.address_id
    join city c on c.city_id = a.city_id
    join country t on c.country_id = t.country_id;
    
-- 7h. List the top five genres in gross revenue in descending order. 
-- (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
select c.category_id, c.name , sum(p.amount) as gross_revenue
from payment p 
	inner join rental r on p.rental_id = r.rental_id
    inner join inventory i on i.inventory_id = r.inventory_id
    inner join film_category f on f.film_id = i.film_id
    inner join category c on c.category_id = f.category_id
group by c.category_id, c.name
order by gross_revenue desc
limit 5;

-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
-- Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query 
-- to create a view.
create view top_five_genres as
select c.category_id, c.name , sum(p.amount) as gross_revenue
from payment p 
	inner join rental r on p.rental_id = r.rental_id
    inner join inventory i on i.inventory_id = r.inventory_id
    inner join film_category f on f.film_id = i.film_id
    inner join category c on c.category_id = f.category_id
group by c.category_id, c.name
order by gross_revenue desc
limit 5;

-- 8b. How would you display the view that you created in 8a?
select * from top_five_genres;

-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
drop view if exists top_five_genres;

