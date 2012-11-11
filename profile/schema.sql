BEGIN;

DROP TABLE IF EXISTS profile CASCADE;
CREATE TABLE profile (
    id              SERIAL PRIMARY KEY,
-- Account info --
    passwd          VARCHAR(32),
    email           VARCHAR(100) UNIQUE,
    enabled         BOOLEAN DEFAULT FALSE,
-- Postal Address Mixin
    country         VARCHAR(50),
    region          VARCHAR(50),
    city            VARCHAR(50),
    address         VARCHAR(50),
    postal_index    VARCHAR(20),
-- Profile Mixin
    avatar          VARCHAR(100),
    name            VARCHAR(20),
    middle_name     VARCHAR(20),
    last_name       VARCHAR(20),
    sex             VARCHAR(1),
    birth_date      DATE,
    about           VARCHAR(1000),
-- CDCMixin --
    date_created    TIMESTAMP default now(),
    date_updated    TIMESTAMP
);


CREATE TRIGGER
  sync_lastmod
BEFORE UPDATE ON
  profile
FOR EACH ROW EXECUTE PROCEDURE
  sync_lastmod();

DROP TABLE IF EXISTS profile_misc CASCADE;
CREATE TABLE profile_misc (
    id              SERIAL PRIMARY KEY,
    entry_id        INTEGER REFERENCES profile(id),
-- Science --
    degree          VARCHAR(30),
    achievement     VARCHAR(1000),
-- Ideology --
    religion        VARCHAR(50),
    political       VARCHAR(50),
    philosophy      VARCHAR(50),
-- Music --
    music_styles    VARCHAR(500),
    favorite_music  VARCHAR(500),
-- Sport --
    sport_styles    VARCHAR(500),
    favorite_sport  VARCHAR(500),
-- Literature --
    literature_styles   VARCHAR(500),
    favorite_literature VARCHAR(500),
-- Cinema --
    cinema_styles   VARCHAR(500),
    favorite_cinema VARCHAR(500),
-- Hobby --
    hobby           VARCHAR(500)
);


DROP TABLE IF EXISTS profile_pager CASCADE;
CREATE TABLE profile_pager (
    id              SERIAL PRIMARY KEY,
    entry_id        INTEGER REFERENCES profile(id),
    name            VARCHAR(10),
    pager           VARCHAR(20)
);


DROP TABLE IF EXISTS profile_phone CASCADE;
CREATE TABLE profile_phone (
    id              SERIAL PRIMARY KEY,
    entry_id        INTEGER REFERENCES profile(id),
    phone_type      VARCHAR(30),
    phone           VARCHAR(30) NOT NULL
);


DROP TABLE IF EXISTS profile_job CASCADE;
CREATE TABLE profile_job (
    id              SERIAL PRIMARY KEY,
    entry_id        INTEGER REFERENCES profile(id),
    is_current      BOOLEAN DEFAULT FALSE,
    name            VARCHAR(100),
    position        VARCHAR(100),
    duty            VARCHAR(500),
    start_from      DATE,
    end_to          DATE,
-- Postal Address Mixin --
    country         VARCHAR(50),
    region          VARCHAR(50),
    city            VARCHAR(50),
    address         VARCHAR(50),
    postal_index    VARCHAR(20)
);


DROP TABLE IF EXISTS profile_university CASCADE;
CREATE TABLE profile_university (
    id              SERIAL PRIMARY KEY,
    entry_id        INTEGER REFERENCES profile(id),
    is_current      BOOLEAN DEFAULT FALSE,
    name            VARCHAR(100),
    faculty         VARCHAR(100),
    cathedra        VARCHAR(100),
    specialty       VARCHAR(100),
    degree          VARCHAR(20),
    start_from      DATE,
    end_to          DATE,
-- Postal Address Mixin --
    country         VARCHAR(50),
    region          VARCHAR(50),
    city            VARCHAR(50),
    address         VARCHAR(50),
    postal_index    VARCHAR(20)
);


DROP TABLE IF EXISTS profile_school CASCADE;
CREATE TABLE profile_school (
    id              SERIAL PRIMARY KEY,
    entry_id        INTEGER REFERENCES profile(id),
    is_current      BOOLEAN DEFAULT FALSE,
    name            VARCHAR(100),
    start_from      DATE,
    end_to          DATE,
-- Postal Address Mixin --
    country         VARCHAR(50),
    region          VARCHAR(50),
    city            VARCHAR(50),
    address         VARCHAR(50),
    postal_index    VARCHAR(20)
);

COMMIT;

-- Initial users registration --
BEGIN;

INSERT INTO profile
(email, passwd)
VALUES
('anonymous', 'no login');

INSERT INTO profile
(email, passwd)
VALUES
('system', 'no login');

INSERT INTO profile
(email, passwd, last_name, middle_name, name, sex)
VALUES
('basha@example.com', 'c7000ad73caf8a4e099e60a61fa6418b', 'Баша', 'Анатольевич', 'Павел', 'm');

INSERT INTO profile
(email, passwd, last_name, middle_name, name, sex)
VALUES
('voropay@example.com', 'c7000ad73caf8a4e099e60a61fa6418b', 'Воропай', 'Юрьевич', 'Михаил', 'm');

INSERT INTO profile
(email, passwd, last_name, middle_name, name, sex)
VALUES
('dronov@example.com', 'c7000ad73caf8a4e099e60a61fa6418b', 'Дронов', 'Александрович', 'Александр', 'm');

INSERT INTO profile
(email, passwd, last_name, middle_name, name, sex)
VALUES
('yalukov.sergey@example.com', 'c7000ad73caf8a4e099e60a61fa6418b', 'Ялуков', 'Батькович', 'Сергей', 'm');

INSERT INTO profile
(email, passwd, last_name, middle_name, name, sex)
VALUES
('yalukov.eugen@example.com', 'c7000ad73caf8a4e099e60a61fa6418b', 'Ялуков', 'Братович', 'Евгений', 'm');

INSERT INTO profile
(email, passwd, last_name, middle_name, name, sex)
VALUES
('maskalev@example.com', 'c7000ad73caf8a4e099e60a61fa6418b', 'Маскалев', 'Батькович', 'Дмитрий', 'm');

INSERT INTO profile
(email, passwd, last_name, middle_name, name, sex)
VALUES
('maskaleva@example.com', 'c7000ad73caf8a4e099e60a61fa6418b', 'Маскалева', 'Батьковна', 'Анна', 'w');

INSERT INTO profile
(email, passwd, last_name, middle_name, name, sex)
VALUES
('meleshko@example.com', 'c7000ad73caf8a4e099e60a61fa6418b', 'Мелешко', 'Батькович', 'Александр', 'm');

INSERT INTO profile
(email, passwd, last_name, middle_name, name, sex)
VALUES
('brat@example.com', 'c7000ad73caf8a4e099e60a61fa6418b', 'Чернецов', 'Михайлович', 'Александр', 'm');

INSERT INTO profile
(email, passwd, last_name, middle_name, name, sex)
VALUES
('xz@example.com', 'c7000ad73caf8a4e099e60a61fa6418b', 'Непонятно', 'кто', 'вообще', 'm');

INSERT INTO profile
(email, passwd, last_name, middle_name, name, sex)
VALUES
('cpu@example.com', 'c7000ad73caf8a4e099e60a61fa6418b', 'Чернецов', 'Михайлович', 'Владимир', 'm');

INSERT INTO profile
(email, passwd, last_name, middle_name, name, sex)
VALUES
('plast@example.com', 'c7000ad73caf8a4e099e60a61fa6418b', 'Пластинин', 'Сергеевич', 'Евгений', 'm');

INSERT INTO profile
(email, passwd, last_name, middle_name, name, sex)
VALUES
('zaxar@example.com', 'c7000ad73caf8a4e099e60a61fa6418b', 'Захарченко', 'Николаевич', 'Сергей', 'm');

COMMIT;

