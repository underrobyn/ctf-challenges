<?php

// Script for initial database creation
if (isset($_SERVER['HTTP_USER_AGENT'])) {
    die('Only allowed to run via command line');
}

require('includes/init.php');

// Connect to database
$dbm = new DatabaseManager();
$db = $dbm->getInstance();

// Create Users table
$db->exec('CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT "GUEST",
    time_created DATETIME DEFAULT CURRENT_TIMESTAMP
)');

$stmt = $db->prepare('INSERT INTO Users (username, email, password, first_name, last_name, age, gender, role) VALUES (:username, :email, :password, :first_name, :last_name, :age, :gender, :role)');


// Define test data
$first_names = array(
    "Michael", "Christopher", "Jessica", "Matthew", "Ashley", "Jennifer", "Joshua", "Amanda", "Daniel", "David",
    "James", "Robert", "John", "Joseph", "Andrew", "Ryan", "Brandon", "Jason", "Justin", "Sarah", "William", "Jonathan",
    "Stephanie", "Brian", "Nicole", "Nicholas", "Anthony", "Heather", "Eric", "Elizabeth", "Adam", "Megan", "Melissa",
    "Kevin", "Steven", "Thomas", "Timothy", "Christina", "Kyle", "Rachel", "Laura", "Lauren", "Amber", "Brittany",
    "Danielle", "Richard", "Kimberly", "Jeffrey", "Amy", "Patrick"
);
$last_names = array(
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Thomas", "Taylor", "Martin", "Bateman",
    "Lee", "Thompson", "White", "Clark", "Lewis", "Robinson", "Walker", "Young", "Hill", "Adams", "Baker", "Acres"
);
$genders = array('Male', 'Female', 'Non-binary');
$roles = array('GUEST', 'USER', 'MODERATOR');
$min_age = 18;
$max_age = 65;

// Insert test users
for ($i = 0; $i < 60; $i++) {
    $first_name = $first_names[array_rand($first_names)];
    $last_name = $last_names[array_rand($last_names)];
    $email = strtolower($first_name . '.' . $last_name . '@corporate.clam-corp.com');
    $password = get_random_str(15);
    $age = mt_rand($min_age, $max_age);
    $gender = $genders[array_rand($genders)];
    $role = $roles[array_rand($roles)];

    $stmt->bindValue(':username', $first_name . $last_name . $i * mt_rand(1, 10), SQLITE3_TEXT);
    $stmt->bindValue(':email', $email, SQLITE3_TEXT);
    $stmt->bindValue(':password', secure_password_hash($password), SQLITE3_TEXT);
    $stmt->bindValue(':first_name', $first_name, SQLITE3_TEXT);
    $stmt->bindValue(':last_name', $last_name, SQLITE3_TEXT);
    $stmt->bindValue(':age', $age, SQLITE3_INTEGER);
    $stmt->bindValue(':gender', $gender, SQLITE3_TEXT);
    $stmt->bindValue(':role', $role, SQLITE3_TEXT);
    $stmt->execute();
}


// Insert admin user
$username = 'admin';
$email = 'superuser@mail.internal.clam-corp.com';
$password = get_random_str(16);

$stmt->bindValue(':username', $username, SQLITE3_TEXT);
$stmt->bindValue(':email', $email, SQLITE3_TEXT);
$stmt->bindValue(':password', secure_password_hash($password), SQLITE3_TEXT); // Hash the password
$stmt->bindValue(':first_name', 'Admin', SQLITE3_TEXT);
$stmt->bindValue(':last_name', 'User', SQLITE3_TEXT);
$stmt->bindValue(':age', 21, SQLITE3_INTEGER);
$stmt->bindValue(':gender', 'Female', SQLITE3_TEXT);
$stmt->bindValue(':role', 'ADMIN', SQLITE3_TEXT);
$stmt->execute();


// Close database connection
$db->close();
