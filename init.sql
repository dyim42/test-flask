BEGIN;

DROP TABLE profile;
CREATE TABLE profile (
    id              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name            VARCHAR(50),
    email           VARCHAR(100) UNIQUE,
    about           VARCHAR(1000),
    passwd          VARCHAR(32),
    birthday        DATE
);


DROP TABLE author;
CREATE TABLE author (
    id              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name            VARCHAR(100)
);


DROP TABLE book;
CREATE TABLE book (
    id              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name            VARCHAR(200)
);

DROP TABLE author_book_mtm;
CREATE TABLE author_book_mtm (
    id              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    author_id       INTEGER REFERENCES author(id),
    book_id         INTEGER REFERENCES book(id)

);


COMMIT;

INSERT INTO profile (id, name, email, about, passwd, birthday) VALUES (1, 'anonymous', 'anonymous', 'This is anonymous user entry.', 'no password', '1901-11-11');
INSERT INTO profile (id, name, email, about, passwd, birthday) VALUES (2, 'Александр Матросов', 'matrossoff@example.com', ' Герой Советского Союза (19.06.1943), красноармеец, стрелок-автоматчик 2-го отдельного батальона 91-й отдельной Сибирской добровольческой бригады имени И. В. Сталина 6-го Сталинского Сибирского добровольческого стрелкового корпуса 22-й армии Калининского фронта, член ВЛКСМ. Известен благодаря самопожертвенному подвигу, когда он закрыл своей грудью амбразуру немецкого дзота. Его подвиг широко освещался в газетах, журналах, литературе, кино и стал в русском языке устойчивым выражением.', 'no password', '1924-05-02');
INSERT INTO profile (id, name, email, about, passwd, birthday) VALUES (3, 'Кожедуб Иван', 'kozhedub@example.com', 'Cоветский военный деятель, лётчик-ас времён Великой Отечественной войны, наиболее результативный лётчик-истребитель в авиации союзников (64 сбитых самолета). Трижды Герой Советского Союза. Маршал авиации', 'no password', '1920-07-08');
INSERT INTO profile (id, name, email, about, passwd, birthday) VALUES (4, 'Гастелло Николай', 'gastello@example.com', 'Cоветский военный лётчик, участник трёх войн, командир 2-й эскадрильи 207-го дальнебомбардировочного авиационного полка 42-й дальнебомбардировочной авиационной дивизии 3-го дальнебомбардировочного авиационного корпуса Дальнебомбардировочной авиации ВВС РККА, капитан. Погиб во время боевого вылета. Герой Советского Союза, посмертно.', 'no password', '1907-12-04');
INSERT INTO profile (id, name, email, about, passwd, birthday) VALUES (5, 'Покрышкин Александр', 'pokrishkin@example.com', ' Cоветский лётчик-ас, второй по результативности (после Ивана Кожедуба) пилот-истребитель среди лётчиков стран антигитлеровской коалиции во Второй мировой войне. Первый Трижды Герой Советского Союза. Маршал авиации', 'no password', '2001-04-12');
INSERT INTO profile (id, name, email, about, passwd, birthday) VALUES (6, 'Будённый Семён', 'budenny@example.com', ' Cоветский военачальник, участник Гражданской войны, командующий Первой Конной армией, один из первых Маршалов Советского Союза, трижды Герой Советского Союза, полный Георгиевский кавалер.', 'no password', '1902-09-09');
INSERT INTO profile (id, name, email, about, passwd, birthday) VALUES (7, 'Гречко Георгий', 'grechko@example.com', ' Cоветский космонавт, дважды Герой Советского Союза. Лётчик-космонавт СССР', 'no password', '1931-12-05');
INSERT INTO profile (id, name, email, about, passwd, birthday) VALUES (8, 'Рубан Петр', 'ruban@example.com', 'Штурман 990-го ночного бомбардировочного авиационного полка 313-й ночной бомбардировочной авиационной дивизии 15-й воздушной армии 2-го Прибалтийского фронта, майор.', 'no password', '1931-12-05');
INSERT INTO profile (id, name, email, about, passwd, birthday) VALUES (9, 'Нахимов Павел', 'naximov@example.com', 'Знаменитый русский адмирал.(хм, википедия немногословна)', 'no password', '1931-12-05');
INSERT INTO profile (id, name, email, about, passwd, birthday) VALUES (10, 'Багратион Павел', 'bagration@example.com', 'российский генерал от инфантерии, командующий 2-й русской армией в начале Отечественной войны 1812 года.', 'no password', '1931-12-05');

INSERT INTO author (id, name) VALUES (1, 'Булгаков, Михаил Афанасьевич');

INSERT INTO book (id, name) VALUES (1, 'Белая гвардия');
INSERT INTO book (id, name) VALUES (2, 'Собачье сердце');
INSERT INTO book (id, name) VALUES (3, 'Мастер и Маргарита');

INSERT INTO author (id, name) VALUES (2, 'Даррелл, Джеральд');

INSERT INTO book (id, name) VALUES (4, 'Перегруженный ковчег (The Overloaded Ark)');
INSERT INTO book (id, name) VALUES (5, 'Гончие Бафута (The Bafut Beagles)');
INSERT INTO book (id, name) VALUES (6, 'Говорящий свёрток (The Talking Parcel)');

INSERT INTO author (id, name) VALUES (3, 'Адамсон, Джой');

INSERT INTO book (id, name) VALUES (7, 'Born Free: A lioness of two worlds');
INSERT INTO book (id, name) VALUES (8, 'Living Free: The story of Elsa and her cubs');
INSERT INTO book (id, name) VALUES (9, 'The Spotted Sphinx');
INSERT INTO book (id, name) VALUES (10, 'Pippa: The Cheetah and her Cubs');
INSERT INTO book (id, name) VALUES (11, 'Peoples of Kenya');






