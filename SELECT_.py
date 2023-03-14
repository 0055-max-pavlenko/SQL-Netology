SELECT genre.genre_name, COUNT(singers.singer_name) count 
  FROM genre
    LEFT JOIN singer_genre 
      ON genre.genre_id = singer_genre.genre_id
    LEFT JOIN singers 
      ON singer_genre.singer_id = singers.singer_id
  GROUP BY genre.genre_name
  ORDER BY count DESC;

SELECT albums.album_name, COUNT(records.record_name) 
  FROM albums
    LEFT JOIN records 
      ON albums.album_id = records.album_id 
    WHERE albums.release_year 
      BETWEEN 2019 AND 2020
  GROUP BY albums.album_name;

SELECT albums.album_name, AVG(records.record_duration) average 
  FROM albums
    LEFT JOIN records 
      ON albums.album_id = records.album_id 
  GROUP BY albums.album_name
  ORDER BY average DESC;

SELECT singer_name 
  FROM singers 
    WHERE singer_name 
      NOT IN
        (SELECT singers.singer_name 
          FROM singers
            FULL JOIN singer_album 
              ON singers.singer_id = singer_album.singer_id
            FULL JOIN albums 
              ON singer_album.album_id = albums.album_id
          WHERE albums.release_year = 2020 
            OR albums.release_year IS NULL);

 
SELECT collections.collection_name 
  FROM collections
    JOIN collection_record 
      ON collections.collection_id = collection_record.collection_id
    JOIN records 
      ON collection_record.record_id = records.record_id
    JOIN albums 
      ON records.album_id = albums.album_id
    JOIN singer_album 
      ON albums.album_id = singer_album.album_id
    JOIN singers 
      ON singer_album.singer_id = singers.singer_id
  WHERE singers.singer_name = 'Muse';

SELECT albums.album_name 
  FROM albums
    JOIN singer_album 
      ON albums.album_id = singer_album.album_id
    JOIN singer_genre 
      ON singer_album.singer_id= singer_genre.singer_id
  WHERE ( SELECT COUNT(DISTINCT singer_genre.genre_id) FROM singer_genre) > 1
  GROUP BY albums.album_name;

SELECT records.record_name 
    FROM records
      FULL JOIN collection_record 
        ON records.record_id = collection_record.record_id
    WHERE collection_record.collection_id IS NULL;

SELECT singers.singer_name 
    FROM singers
      JOIN singer_album 
        ON singers.singer_id = singer_album.singer_id
      JOIN albums 
        ON singer_album.album_id = albums.album_id
      JOIN records 
        ON albums.album_id = records.album_id
      WHERE records.record_duration = (SELECT MIN(records.record_duration) FROM records)
    GROUP BY singers.singer_name;

SELECT album_name 
    FROM albums
      JOIN records ON albums.album_id = records.album_id
        GROUP BY album_name
        HAVING COUNT(album_name) = 
          (SELECT COUNT(album_name) count 
            FROM albums
              JOIN records 
                ON albums.album_id = records.album_id
              GROUP BY album_name
              ORDER BY count
              LIMIT 1);




