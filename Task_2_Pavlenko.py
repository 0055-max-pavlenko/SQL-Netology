CREATE TABLE IF NOT EXISTS records (
		record_id SERIAL PRIMARY KEY,
		record_name VARCHAR(80) NOT NULL,
		record_duration TIME NOT NULL,
		album_id INTEGER NOT NULL REFERENCES albums(album_id)
);
CREATE TABLE IF NOT EXISTS albums (
		album_id SERIAL PRIMARY KEY,
		album_name VARCHAR(80) NOT NULL,
		release_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS singer_album(
		id SERIAL PRIMARY KEY,
		singer_id INTEGER NOT NULL REFERENCES singers(singer_id),
		album_id INTEGER NOT NULL REFERENCES albums(album_id)
);

CREATE TABLE IF NOT EXISTS singers (
		singer_id SERIAL PRIMARY KEY,
		singer_name VARCHAR(80)
);

CREATE TABLE IF NOT EXISTS singer_genre(
		id SERIAL PRIMARY KEY,
		genre_id INTEGER NOT NULL REFERENCES genre(genre_id),
		singer_id INTEGER NOT NULL REFERENCES singers(singer_id)
);

CREATE TABLE IF NOT EXISTS genre(
		genre_id SERIAL PRIMARY KEY,
		genre_name VARCHAR(80)
);

CREATE TABLE IF NOT EXISTS collection_record(
		id SERIAL PRIMARY KEY,
		collection_id INTEGER NOT NULL REFERENCES collections(collection_id),
		record_id INTEGER NOT NULL REFERENCES records(record_id)
);

CREATE TABLE IF NOT EXISTS collections(
		collection_id SERIAL PRIMARY KEY,
		collection_name VARCHAR(80),
		release_year INTEGER NOT NULL
);

