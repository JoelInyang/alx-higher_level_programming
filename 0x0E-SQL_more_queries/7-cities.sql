-- create database hbtn_0d_usa and table 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE NOT NULL, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FORIEGN KEY(state_id) REFERENCES states(id), PRIMARY KEY(id));
