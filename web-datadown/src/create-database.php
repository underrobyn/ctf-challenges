<?php

// Script for initial database creation
if (isset($_SERVER['HTTP_USER_AGENT'])) {
    die('Only allowed to run via command line');
}

require('includes/init.php');

// SQLite database file path
$db_file = 'users.db';

// Create or open database
$db = new SQLite3($db_file);

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
$email = 'admin@admin.com';
$password = file_get_contents('/flag.txt');

$stmt = $db->prepare('INSERT INTO Users (username, email, password) VALUES (:username, :email, :password)');

$stmt->bindValue(':username', $username, SQLITE3_TEXT);
$stmt->bindValue(':email', $email, SQLITE3_TEXT);
$stmt->bindValue(':password', secure_password_hash($password), SQLITE3_TEXT); // Hash the password
$stmt->execute();


// Close database connection
$db->close();
