create database python_mysql;
show create table python_mysql.user;

CREATE TABLE python_mysql.user (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) DEFAULT '',
  `sex` varchar(10) DEFAULT '',
  `age` int(11) DEFAULT '0',
  `email` varchar(128) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='user table'

insert into python_mysql.user (name, sex, age, email) values ('xiaomei','woman',18,'xiaomei@qq.com');
