use big_project;
 
create table movies (
    id int NOT NULL AUTO_INCREMENT,
    title varchar(250),
    director varchar(250),
    year int,
    PRIMARY KEY(id)
    ); 