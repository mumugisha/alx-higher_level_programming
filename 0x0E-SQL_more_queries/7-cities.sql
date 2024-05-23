-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Switch to the newly created database
USE `hbtn_0d_usa`;

-- Create the table `states` if it doesn't already exist
CREATE TABLE IF NOT EXISTS `states` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL
);

-- Create the table `cities` if it doesn't already exist
CREATE TABLE IF NOT EXISTS `cities` (
    `id` INT NOT NULL UNIQUE AUTO_INCREMENT,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`state_id`) REFERENCES `states`(`id`)
);
