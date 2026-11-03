CREATE DATABASE jiohotstar_analysis;
USE jiohotstar_analysis;

SELECT COUNT(*)
FROM hotstar_content
WHERE content_type = 'Movie';

SELECT COUNT(*)
FROM hotstar_content
WHERE content_type = 'TV Show';

SELECT genre, COUNT(*) AS total_titles
FROM hotstar_content
GROUP BY genre
ORDER BY total_titles DESC;

SELECT language, COUNT(*) AS highest_number_of_title
FROM hotstar_content
GROUP BY language
ORDER BY highest_number_of_title DESC
LIMIT 1;

SELECT AVG(imdb_rating)
FROM hotstar_content;

SELECT release_year, COUNT(*) AS highest_count
FROM hotstar_content
GROUP BY release_year
ORDER BY highest_count DESC
LIMIT 1;

SELECT age_rating, COUNT(*) AS count_title
FROM hotstar_content
GROUP BY age_rating
ORDER BY count_title ASC;

SELECT genre, AVG(imdb_rating) AS avg_rating
FROM hotstar_content
GROUP BY genre
ORDER BY avg_rating DESC
LIMIT 1;

SELECT content_type, AVG(imdb_rating) AS avg_rating
FROM hotstar_content
GROUP BY content_type;

SELECT country, COUNT(*) AS count_title
FROM hotstar_content
GROUP BY country
ORDER BY count_title DESC
LIMIT 1;

SELECT AVG(duration_minutes) AS avg_duration_minutes
FROM hotstar_content
WHERE content_type = 'Movie';

SELECT TITLE, DURATION_MINUTES
FROM HOTSTAR_CONTENT
WHERE CONTENT_TYPE = 'Movie'
ORDER BY DURATION_MINUTES DESC
LIMIT 1;

SELECT title, imdb_rating
FROM hotstar_content
WHERE content_type = 'Movie'
ORDER BY imdb_rating DESC
LIMIT 1;

SELECT title, imdb_rating
FROM hotstar_content
WHERE content_type = 'TV Show'
ORDER BY imdb_rating ASC
LIMIT 1;

SELECT title, release_year, imdb_rating
FROM hotstar_content
WHERE content_type = 'Movie'
AND release_year > 2020
ORDER BY release_year DESC;

SELECT title, seasons, episodes, imdb_rating
FROM hotstar_content
WHERE content_type = 'TV Show'
AND seasons > 1
ORDER BY seasons DESC;

SELECT title, content_type, imdb_rating
FROM hotstar_content
ORDER BY imdb_rating DESC
LIMIT 5;

SELECT title, content_type, imdb_rating
FROM hotstar_content
WHERE imdb_rating > (
    SELECT AVG(imdb_rating)
    FROM hotstar_content
)
ORDER BY imdb_rating DESC;

SELECT genre, AVG(imdb_rating) AS avg_rating
FROM hotstar_content
GROUP BY genre
HAVING AVG(imdb_rating) > (
    SELECT AVG(imdb_rating)
    FROM hotstar_content
)
ORDER BY avg_rating DESC;

SELECT content_type, AVG(imdb_rating) AS avg_rating
FROM hotstar_content
GROUP BY content_type
HAVING AVG(imdb_rating) > 7
ORDER BY avg_rating DESC;

SELECT language, COUNT(*) AS total_titles
FROM hotstar_content
GROUP BY language
HAVING COUNT(*) > 10
ORDER BY total_titles DESC;

SELECT country, COUNT(*) AS total_titles
FROM hotstar_content
GROUP BY country
HAVING COUNT(*) > 5
ORDER BY total_titles DESC;

SELECT language, AVG(imdb_rating) AS avg_rating
FROM hotstar_content
GROUP BY language
ORDER BY avg_rating DESC;

SELECT title, release_year, content_type
FROM hotstar_content
WHERE release_year BETWEEN 2018 AND 2022
ORDER BY release_year DESC;

SELECT title, imdb_rating, content_type
FROM hotstar_content
WHERE imdb_rating BETWEEN 7 AND 8
ORDER BY imdb_rating DESC;

SELECT title, duration_minutes, imdb_rating
FROM hotstar_content
WHERE content_type = 'Movie'
AND duration_minutes BETWEEN 90 AND 150
ORDER BY duration_minutes DESC;

SELECT title, content_type, duration_minutes
FROM hotstar_content
WHERE duration_minutes IS NULL;

SELECT genre, COUNT(*) AS total_titles,
       AVG(imdb_rating) AS avg_rating
FROM hotstar_content
GROUP BY genre
HAVING COUNT(*) > 5
ORDER BY avg_rating DESC;