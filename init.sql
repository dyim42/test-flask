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
    name            VARCHAR(100)
);

COMMIT;

INSERT INTO profile (name, email, about, passwd, birthday) VALUES ('anonymous', 'anonymous', 'This is anonymous user entry.', 'no password', '1901-11-11');
INSERT INTO profile (name, email, about, passwd, birthday) VALUES ('Александр Матросов', 'matrossoff@example.com', ' Герой Советского Союза (19.06.1943), красноармеец, стрелок-автоматчик 2-го отдельного батальона 91-й отдельной Сибирской добровольческой бригады имени И. В. Сталина 6-го Сталинского Сибирского добровольческого стрелкового корпуса 22-й армии Калининского фронта, член ВЛКСМ. Известен благодаря самопожертвенному подвигу, когда он закрыл своей грудью амбразуру немецкого дзота. Его подвиг широко освещался в газетах, журналах, литературе, кино и стал в русском языке устойчивым выражением.', 'no password', '1924-05-02');
INSERT INTO profile (name, email, about, passwd, birthday) VALUES ('Кожедуб Иван', 'kozhedub@example.com', 'Cоветский военный деятель, лётчик-ас времён Великой Отечественной войны, наиболее результативный лётчик-истребитель в авиации союзников (64 сбитых самолета). Трижды Герой Советского Союза. Маршал авиации', 'no password', '1920-07-08');
INSERT INTO profile (name, email, about, passwd, birthday) VALUES ('Гастелло Николай', 'gastello@example.com', 'Cоветский военный лётчик, участник трёх войн, командир 2-й эскадрильи 207-го дальнебомбардировочного авиационного полка 42-й дальнебомбардировочной авиационной дивизии 3-го дальнебомбардировочного авиационного корпуса Дальнебомбардировочной авиации ВВС РККА, капитан. Погиб во время боевого вылета. Герой Советского Союза, посмертно.', 'no password', '1907-12-04');
INSERT INTO profile (name, email, about, passwd, birthday) VALUES ('Покрышкин Александр', 'pokrishkin@example.com', ' Cоветский лётчик-ас, второй по результативности (после Ивана Кожедуба) пилот-истребитель среди лётчиков стран антигитлеровской коалиции во Второй мировой войне. Первый Трижды Герой Советского Союза. Маршал авиации', 'no password', '2001-04-12');
INSERT INTO profile (name, email, about, passwd, birthday) VALUES ('Будённый Семён', 'budenny@example.com', ' Cоветский военачальник, участник Гражданской войны, командующий Первой Конной армией, один из первых Маршалов Советского Союза, трижды Герой Советского Союза, полный Георгиевский кавалер.', 'no password', '1902-09-09');
INSERT INTO profile (name, email, about, passwd, birthday) VALUES ('Гречко Георгий', 'grechko@example.com', ' Cоветский космонавт, дважды Герой Советского Союза. Лётчик-космонавт СССР', 'no password', '1931-12-05');
INSERT INTO profile (name, email, about, passwd, birthday) VALUES ('Рубан Петр', 'ruban@example.com', 'Штурман 990-го ночного бомбардировочного авиационного полка 313-й ночной бомбардировочной авиационной дивизии 15-й воздушной армии 2-го Прибалтийского фронта, майор.', 'no password', '1931-12-05');
INSERT INTO profile (name, email, about, passwd, birthday) VALUES ('Нахимов Павел', 'naximov@example.com', 'Знаменитый русский адмирал.(хм, википедия немногословна)', 'no password', '1931-12-05');
INSERT INTO profile (name, email, about, passwd, birthday) VALUES ('Багратион Павел', 'bagration@example.com', 'российский генерал от инфантерии, командующий 2-й русской армией в начале Отечественной войны 1812 года.', 'no password', '1931-12-05');

INSERT INTO author (name) VALUES ('Булгаков, Михаил Афанасьевич');

INSERT INTO book (name) VALUES ('Белая гвардия');
INSERT INTO book (name) VALUES ('Собачье сердце');
INSERT INTO book (name) VALUES ('Мастер и Маргарита');

INSERT INTO author (name) VALUES ('Даррелл, Джеральд');

INSERT INTO book (name) VALUES ('Перегруженный ковчег (The Overloaded Ark)');
INSERT INTO book (name) VALUES ('Гончие Бафута (The Bafut Beagles)');
INSERT INTO book (name) VALUES ('Говорящий свёрток (The Talking Parcel)');

INSERT INTO author (name) VALUES ('Адамсон, Джой');

INSERT INTO book (name) VALUES ('Born Free: A lioness of two worlds');
INSERT INTO book (name) VALUES ('Living Free: The story of Elsa and her cubs');
INSERT INTO book (name) VALUES ('The Spotted Sphinx');
INSERT INTO book (name) VALUES ('Pippa: The Cheetah and her Cubs');
INSERT INTO book (name) VALUES ('Peoples of Kenya');






