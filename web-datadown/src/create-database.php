<?php

// Script for initial database creation
if (isset($_SERVER['HTTP_USER_AGENT'])) {
    die('Only allowed to run via command line');
}

require('includes/init.php');

// Connect to database
$dbm = new database();
$db = $dbm->getInstance();

// Create Users table
$db->exec('CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    time_created DATETIME DEFAULT CURRENT_TIMESTAMP
)');


// Insert admin user
$username = 'admin';
$email = 'flagmaster@localhost.localdomain';
$password = get_random_str(8);

$stmt = $db->prepare('INSERT INTO Users (username, email, password) VALUES (:username, :email, :password)');

$stmt->bindValue(':username', $username, SQLITE3_TEXT);
$stmt->bindValue(':email', $email, SQLITE3_TEXT);
$stmt->bindValue(':password', secure_password_hash($password), SQLITE3_TEXT); // Hash the password
$stmt->execute();


// Close database connection
$db->close();
