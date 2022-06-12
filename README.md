# MySQL-CRUD-Flask-NOteo

Basic command in MySQL

## -- create 

create database sabari;
show databases;
use python;
show tables;
create table primary_table (id int unsigned auto_increment,username varchar(100),email varchar(100),primary key(id));

## -- Read
select * from python_table;

## -- Update
insert into primary_table (username,email)
values('ram','ram@gmail.com');


## -- Delete
delete from sabari_table where username='sabari';
truncate sabari_table;
drop table primary_table;
