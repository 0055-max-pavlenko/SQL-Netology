SELECT album_name, release_year FROM albums
WHERE release_year = 2018;

SELECT record_name, record_duration FROM records
ORDER BY record_duration DESC
LIMIT 1;

SELECT record_name FROM records
WHERE record_duration >= '00:03:30';

SELECT collection_name FROM collections
WHERE release_year BETWEEN 2018 AND 2020;

SELECT singer_name FROM singers
WHERE singer_name NOT LIKE '% %';

SELECT record_name FROM records
WHERE record_name LIKE ANY (ARRAY ['мой %', '% мой %', '% мой',
'Мой %', '% Мой %', '% Мой',
'my %', '% my %', '% my',
'My %', '% My %', '% My']);

