--
-- Файл сгенерирован с помощью SQLiteStudio v3.3.3 в Вс сен 26 23:37:28 2021
--
-- Использованная кодировка текста: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: access
DROP TABLE IF EXISTS access;

CREATE TABLE access (
    id       INTEGER    PRIMARY KEY AUTOINCREMENT,
    idUser   BIGINT     REFERENCES users (id) ON DELETE RESTRICT,
    datetime DATETIME,
    [select] CHAR (300),
    idRole   BIGINT     REFERENCES roles (id) ON DELETE RESTRICT
);


-- Таблица: courses
DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
    id      INTEGER       PRIMARY KEY AUTOINCREMENT,
    name    CHAR (100),
    volume  INTEGER       DEFAULT (0),
    lesson  INTEGER       DEFAULT (0),
    url     VARCHAR (200),
    year    INTEGER       DEFAULT (2021),
    Target  CHAR (20),
    comment CHAR (100)    DEFAULT ('') 
);


-- Таблица: group_table
DROP TABLE IF EXISTS group_table;

CREATE TABLE group_table (
    id       INTEGER    PRIMARY KEY AUTOINCREMENT,
    idGroups BIGINT     REFERENCES [groups] (id) ON DELETE RESTRICT
                                                 ON UPDATE NO ACTION,
    idUsers  BIGINT     REFERENCES users (id) ON DELETE RESTRICT
                                              ON UPDATE NO ACTION,
    comment  CHAR (200) DEFAULT ('') 
);


-- Таблица: groups
DROP TABLE IF EXISTS [groups];

CREATE TABLE [groups] (
    id        INTEGER    PRIMARY KEY AUTOINCREMENT,
    name      CHAR (30),
    idUsers   INTEGER    REFERENCES users (id) ON DELETE CASCADE
                                               ON UPDATE NO ACTION,
    idCourses INTEGER    REFERENCES courses (id) ON DELETE CASCADE
                                                 ON UPDATE NO ACTION,
    comment   CHAR (100) DEFAULT ('') 
);


-- Таблица: journals
DROP TABLE IF EXISTS journals;

CREATE TABLE journals (
    id       INTEGER     PRIMARY KEY AUTOINCREMENT,
    idGroups BIGINT      REFERENCES [groups] (id) ON DELETE RESTRICT
                                                  ON UPDATE NO ACTION,
    date     DATE,
    idUsers  BIGINT      REFERENCES users (id) ON DELETE RESTRICT
                                               ON UPDATE NO ACTION,
    pres     INTEGER (1) DEFAULT (2),
    [range]  INTEGER     DEFAULT (0),
    shtraf   CHAR (10), 
    comment   CHAR (100) DEFAULT ('') 
);


-- Таблица: log
DROP TABLE IF EXISTS log;

CREATE TABLE log (
    id   INTEGER    PRIMARY KEY AUTOINCREMENT,
    name CHAR (100),
    date BLOB (20),
    time CHAR (20),
    info CHAR (200),
    uid  CHAR (10) 
);


-- Таблица: places
DROP TABLE IF EXISTS places;

CREATE TABLE places (
    id      INTEGER    PRIMARY KEY AUTOINCREMENT,
    name    CHAR (200),
    comment CHAR (20)  DEFAULT ('') 
);


-- Таблица: priv
DROP TABLE IF EXISTS priv;

CREATE TABLE priv (
    id      INTEGER    PRIMARY KEY AUTOINCREMENT,
    name    CHAR (40),
    access  CHAR (10),
    comment CHAR (100) DEFAULT ('') 
);


-- Таблица: roles
DROP TABLE IF EXISTS roles;

CREATE TABLE roles (
    id      INTEGER    PRIMARY KEY AUTOINCREMENT,
    name    CHAR (200),
    idPriv  BIGINT     REFERENCES priv (id) ON DELETE RESTRICT
                                            ON UPDATE NO ACTION,
    comment CHAR (100) DEFAULT ('') 
);


-- Таблица: users
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    fam         CHAR (40),
    ima         CHAR (40),
    otch        CHAR (40),
    phone       CHAR (11),
    email       CHAR (40),
    birthday    DATE,
    comment     CHAR (200) DEFAULT (''),
    idRoles     BIGINT     REFERENCES roles (id) ON DELETE RESTRICT
                                                 ON UPDATE NO ACTION,
    idPlaces    BIGINT     REFERENCES places (id) ON DELETE RESTRICT
                                                  ON UPDATE NO ACTION,
    name        TEXT (50),
    passwd      BLOB (400),
    login       CHAR (30),
    sertificate CHAR (20),
    id          INTEGER    PRIMARY KEY AUTOINCREMENT,
    CONSTRAINT FK_users_places FOREIGN KEY (
        idPlaces
    )
    REFERENCES places (id) ON DELETE RESTRICT,
    CONSTRAINT FK_users_roles_2 FOREIGN KEY (
        idRoles
    )
    REFERENCES roles (id) ON DELETE RESTRICT
);


-- Индекс: users_name
DROP INDEX IF EXISTS users_name;

CREATE UNIQUE INDEX users_name ON users (
    name
);


-- Триггер: courses_in_groups
DROP TRIGGER IF EXISTS courses_in_groups;
CREATE TRIGGER courses_in_groups
        BEFORE DELETE
            ON courses
      FOR EACH ROW
          WHEN (
                   SELECT count( * ) 
                     FROM [groups]
                    WHERE idCourses = OLD.id
               )
> 0
BEGIN
    SELECT RAISE(ABORT, "groups data used");
END;


-- Триггер: groups_in_group_table
DROP TRIGGER IF EXISTS groups_in_group_table;
CREATE TRIGGER groups_in_group_table
        BEFORE DELETE
            ON [groups]
      FOR EACH ROW
          WHEN (
                   SELECT count( * ) 
                     FROM group_table
                    WHERE idGroups = OLD.id
               )
> 0
BEGIN
    SELECT RAISE(ABORT, "grou_table data used");
END;


-- Триггер: groups_in_journal
DROP TRIGGER IF EXISTS groups_in_journal;
CREATE TRIGGER groups_in_journal
        BEFORE DELETE
            ON [groups]
      FOR EACH ROW
          WHEN (
                   SELECT count( * ) 
                     FROM journals
                    WHERE idGroups = OLD.id
               )
> 0
BEGIN
    SELECT RAISE(ABORT, "journals data used");
END;


-- Триггер: places_in_users
DROP TRIGGER IF EXISTS places_in_users;
CREATE TRIGGER places_in_users
        BEFORE DELETE
            ON places
      FOR EACH ROW
          WHEN (
                   SELECT count( * ) 
                     FROM users
                    WHERE idPlaces = OLD.id
               )
> 0
BEGIN
    SELECT RAISE(ABORT, "users data used");
END;


-- Триггер: priv_in_roles
DROP TRIGGER IF EXISTS priv_in_roles;
CREATE TRIGGER priv_in_roles
        BEFORE DELETE
            ON priv
      FOR EACH ROW
          WHEN (
                   SELECT count( * ) 
                     FROM roles
                    WHERE idPriv = OLD.id
               )
> 0
BEGIN
    SELECT RAISE(ABORT, "roles data used");
END;


-- Триггер: roles_in_users
DROP TRIGGER IF EXISTS roles_in_users;
CREATE TRIGGER roles_in_users
        BEFORE DELETE
            ON roles
      FOR EACH ROW
          WHEN (
                   SELECT count( * ) 
                     FROM users
                    WHERE idRoles = OLD.id
               )
> 0
BEGIN
    SELECT RAISE(ABORT, "users data used");
END;


-- Триггер: users_in_group
DROP TRIGGER IF EXISTS users_in_group;
CREATE TRIGGER users_in_group
        BEFORE DELETE
            ON users
      FOR EACH ROW
          WHEN (
                   SELECT count( * ) 
                     FROM [groups]
                    WHERE idUsers = OLD.id
               )
> 0
BEGIN
    SELECT RAISE(ABORT, "group data used");
END;


-- Триггер: users_in_group_table
DROP TRIGGER IF EXISTS users_in_group_table;
CREATE TRIGGER users_in_group_table
        BEFORE DELETE
            ON users
      FOR EACH ROW
          WHEN (
                   SELECT count( * ) 
                     FROM group_table
                    WHERE idUsers = OLD.id
               )
> 0
BEGIN
    SELECT RAISE(ABORT, "group_table data used");
END;


-- Триггер: users_in_journals
DROP TRIGGER IF EXISTS users_in_journals;
CREATE TRIGGER users_in_journals
        BEFORE DELETE
            ON users
      FOR EACH ROW
          WHEN (
                   SELECT count( * ) 
                     FROM journals
                    WHERE idUsers = OLD.id
               )
> 0
BEGIN
    SELECT RAISE(ABORT, "journals data used");
END;


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
