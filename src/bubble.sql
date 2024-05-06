DROP DATABASE IF EXISTS bubble;
CREATE DATABASE IF NOT EXISTS bubble;
USE bubble;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE user (
  id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  mail VARCHAR(50) NOT NULL,
  nom VARCHAR(50) NOT NULL,
  prenom VARCHAR(50) NOT NULL,
  adresse VARCHAR(90) NOT NULL,
  motdepasse VARCHAR(150) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  statut VARCHAR(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO user (mail, nom, prenom, adresse, motdepasse, statut) VALUES
('eve@gmail.com', 'Eve','eve','eve','eve','admin'),
('olivia@gmail.com', 'Olivia','olivia','olivia','olivia','admin');


CREATE TABLE `product` (
  id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  identifier VARCHAR(50) NOT NULL,
  price double(11,2) DEFAULT '0.00' NOT NULL,
  def VARCHAR(50) NOT NULL,
  stock int(11) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO product (identifier, price, def, stock) VALUES
('black tea', '10.00','Thé noir au lait',50),
('green tea', '9.00','Thé vert',50);


CREATE TABLE `divers_product` (
  id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  identifier VARCHAR(50) NOT NULL,
  price double(11,2) DEFAULT '0.00' NOT NULL,
  def VARCHAR(50) NOT NULL,
  stock int(11) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO divers_product (identifier, price, def, stock) VALUES
('Tapioca', '2.00', "Tapioca d'Asie",50),
('Perle mangue', '2.00','Thé vert',50),
('Gelée lychee', '2.00','Thé vert',50),
('Sucre 0%', '0.00','Sans sucre',50),
('Sucre 25%', '0.00','Environ 7g de sucre',50),
('Sucre 50%', '0.00','Environ 15g de sucre',50),
('Sucre 75%', '0.00','Environ 22g de sucre',50),
('Sucre 100%', '0.00','Environ 30g de sucre',50);



CREATE TABLE `panier` (
  id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_user int(11) REFERENCES user(id),
  id_product int(11) REFERENCES product(id),
  id_divers_product int(11) REFERENCES divers_product(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  price double(11,2) DEFAULT '0.00' NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO panier (price) VALUES
('9');




