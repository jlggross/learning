/* ----------------------------------------------------------------- */
/* Keyword SELECT and FROM */
/* ----------------------------------------------------------------- */
SELECT names
FROM people; /* Select just column 'names' from table 'people' */

SELECT names, address
FROM people; /* Select columns 'names' and 'address' from table 'people' */

SELECT *
FROM people; /* Select all columns from table 'people' */

/* ----------------------------------------------------------------- */
/* Keyword LIMIT */
/* ----------------------------------------------------------------- */
SELECT *
FROM people
LIMIT 10; /* Select all columns from table 'table', but return just 10 results */

/* ----------------------------------------------------------------- */
/* Keyword DISTINCT */
/* ----------------------------------------------------------------- */
SELECT DISTINCT names
FROM people; /* Select all unique names from table column 'names' */

/* ----------------------------------------------------------------- */
/* Keyword COUNT */
/* ----------------------------------------------------------------- */
SELECT COUNT(*)
FROM people; /* Count the number of rows from table 'people' */

SELECT COUNT(birthdate)
FROM people; /* Count the number of birth dates in column 'birthdate' */

SELECT COUNT(DISTINCT birthdate)
FROM people; /*Count the number of unique birth dates in column 'birthdate'*/

/* ----------------------------------------------------------------- */
/* Keyword WHERE, AND, OR */
/* ----------------------------------------------------------------- */
= equal
<> not equal
< less than
> greater than
<= less than or equal to
>= greater than or equal to

SELECT title
FROM films
WHERE title = 'Metropolis'; /* Filter title by name 'Metropolis' */

SELECT title, release_year
FROM films
WHERE release_year > 2000;

SELECT title
FROM films
WHERE release_year > 1994
AND release_year < 2000;

/* ----------------------------------------------------------------- */
/* Keyword BETWEEN */
/* ----------------------------------------------------------------- */
SELECT title
FROM films
WHERE release_year
BETWEEN 1994 AND 2000; /* Includes dates 1994 and 2000 */

/* ----------------------------------------------------------------- */
/* Keyword IN */
/* ----------------------------------------------------------------- */
SELECT name
FROM kids
WHERE age = 2
OR age = 4
OR age = 6
OR age = 8
OR age = 10;

SELECT name
FROM kids
WHERE age IN (2, 4, 6, 8, 10);

SELECT title, certification
FROM films
WHERE certification IN ('NC-17', 'R')

/* ----------------------------------------------------------------- */
/* Keyword IS NULL */
/* ----------------------------------------------------------------- */
SELECT COUNT(*)
FROM people
WHERE birthdate IS NULL;

SELECT title 
FROM films
WHERE budget IS NOT NULL

/* ----------------------------------------------------------------- */
/* Keyword LIKR */
/* ----------------------------------------------------------------- */

/* wildcards */
% : match zero, one or many characters in text
_ : match a single character

SELECT name
FROM companies
WHERE name LIKE 'Data%'; /* Match 'Data', 'DataC' 'DataCamp', 'DataMind' */

SELECT name
FROM companies
WHERE name LIKE 'DataC_mp'; /* Match 'DataCamp', 'DataComp' */

select name
from people 
where name like '_r%' /* Get the names of people whose names have 'r' as the second letter. The pattern you need is '_r%'. */

/* ----------------------------------------------------------------- */
/* Aggregate functions */
/* ----------------------------------------------------------------- */
SELECT AVG(budget)
FROM films;

SELECT MAX(budget)
FROM films;

SELECT SUM(budget)
FROM films;

/* ----------------------------------------------------------------- */
/* Aggregate functions */
/* ----------------------------------------------------------------- */
SELECT (4 * 3); /* 12 */

SELECT (4 / 3); /* 1 */

SELECT (4.0 / 3.0) AS result; /* 1.33333 */

/* ----------------------------------------------------------------- */
/* Keyword AS (Alias) */
/* ----------------------------------------------------------------- */
SELECT MAX(budget) AS max_budget,
       MAX(duration) AS max_duration
FROM films;

/* ----------------------------------------------------------------- */
/* Keyword ORDER BY, DESC  */
/* ----------------------------------------------------------------- */
SELECT title
FROM films
ORDER BY release_year DESC;

SELECT birthdate, name
FROM people
ORDER BY birthdate, name; /* Multiple sorting columns */

/* ----------------------------------------------------------------- */
/* Keyword GROUP BY  */
/* ----------------------------------------------------------------- */
SELECT sex, count(*)
FROM employees
GROUP BY sex;

-- Commonly, GROUP BY is used with aggregate functions like COUNT() or MAX()

SELECT sex, count(*)
FROM employees
GROUP BY sex
ORDER BY count DESC; -- Group By comes before Order By

/* ----------------------------------------------------------------- */
/* Keyword HAVING  */
/* ----------------------------------------------------------------- */

-- HAVING is used to filter based on the result of an aggregate function. 

/* Invalid query - don't work with WHERE */
SELECT release_year
FROM films
GROUP BY release_year
WHERE COUNT(title) > 10;

/* Valid query */
SELECT release_year
FROM films
GROUP BY release_year
HAVING COUNT(title) > 10;

/* ----------------------------------------------------------------- */
/* Complete examples  */
/* ----------------------------------------------------------------- */

/* Example 1 */
select release_year, avg(budget) as avg_budget, avg(gross) as avg_gross
from films
where release_year > 1990
group by release_year
having avg(budget) > 60000000
order by avg_gross desc

/* Example 2 */
select country, avg(budget) as avg_budget, avg(gross) as avg_gross
from films
group by country
having count(*) > 10
order by country
limit 5







