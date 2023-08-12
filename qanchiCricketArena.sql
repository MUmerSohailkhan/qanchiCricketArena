-- create database qanchiCricketArena
-- drop database qanchicricketarena
-- use  qanchiCricketarena;
-- create table employees(
-- empId varchar(25),empName varchar(25),phoneNo char(15),hireDate varchar(10),sex  char(10),birthdate char(10),salary int,bonus int);
-- create table newEmpolyeeTable as 
-- select  empName,phoneNo from employees;
drop table manager;

-- ---------------------------------------------ALTER------------------------------------------------------
-- alter table  employees add column fathername  varchar(25);
-- alter table employees   drop column  fathername;
-- alter table employees modify column birthdate  date;
alter table employees add constraint ucperson unique (empid);
alter table employees add constraint pk_employee primary key (empId);


create table manager(
manId varchar(25) not null unique, manName varchar(25) not null);
