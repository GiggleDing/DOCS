DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS docx;
DROP TABLE IF EXISTS paragraph;
DROP TABLE IF EXISTS run;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE docx (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE paragraph (
    id INTEGER PRIMARY KEY,
    style TEXT,
    docx_id INTEGER NOT NULL,
    FOREIGN KEY (docx_id) REFERENCES docx (id)
);

CREATE TABLE run (
    id INTEGER PRIMARY KEY,
    text TEXT,
    style TEXT,
    bold INTEGER,
    color TEXT,
    paragraph_id INTEGER NOT NULL,
    FOREIGN KEY (paragraph_id) REFERENCES paragraph(id)
);