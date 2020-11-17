CREATE DATABASE blog_DB;
use blog_DB;

CREATE TABLE IF NOT EXISTS posts (
  id_post INT(4) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  contenu VARCHAR(200),
  ip_auteur VARCHAR(20),
  date_heure_post DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO posts(contenu, ip_auteur) VALUES ("salut tout le monde !","192.1.1.4");
INSERT INTO posts(contenu, ip_auteur) VALUES ("Aujourd'hui on fait des tests","192.1.1.4");