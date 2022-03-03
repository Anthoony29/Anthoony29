DROP TABLE IF EXISTS posts;

CREATE TABLE cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    price INTEGER NOT NULL,
    shifter TEXT  NOT NULL,
    transmission TEXT NOT NULL,
    consumption TEXT NOT NULL,
    motorPower TEXT NOT NULL,
    emissionCO2 TEXT NOT NULL
);

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    username TEXT,
    email TEXT,
    password TEXT,
)

CREATE TABLE concept (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    name TEXT,
    image TEXT,
    lien TEXT
)