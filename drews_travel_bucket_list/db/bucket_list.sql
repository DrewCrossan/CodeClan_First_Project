DROP TABLE IF EXISTS sights;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    continent VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    visited BOOLEAN,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE sights (
    id SERIAL PRIMARY KEY,
    sight_name VARCHAR(255),
    description TEXT,
    visited BOOLEAN,
    city_id INT REFERENCES cities(id) ON DELETE CASCADE
);