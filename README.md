# MySQL-CRUD-Flask-NOteo

Basic command in MySQL



  

## -- create 
```
create database sabari;
show databases;
use sabari;
show tables;
create table primary_table (id int unsigned auto_increment,username varchar(100),email varchar(100),primary key(id));
```
## -- Read
```
select * from primary_table;
```

## -- Update
```
insert into primary_table (username,email)
values('ram','ram@gmail.com');
```

## -- Delete
```
delete from primary_table where username='sabari';
truncate primary_table;
drop table primary_table;
```
