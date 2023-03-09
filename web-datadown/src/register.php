<?php

require('includes/init.php');

check_user_anonymous();

// SQLite database file path
$db_file = 'users.db';

// Get registration form data
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Connect to database
    $db = new SQLite3($db_file);

    // Check if username or email already exists
    $stmt = $db->prepare('SELECT COUNT(*) FROM Users WHERE username = :username OR email = :email');

    $stmt->bindValue(':username', $username, SQLITE3_TEXT);
    $stmt->bindValue(':email', $email, SQLITE3_TEXT);

    $result = $stmt->execute();
    $count = $result->fetchArray(SQLITE3_NUM)[0];

    if ($count > 0) {
        echo 'Username or email already exists';
    } else {
        // Insert new user
        $stmt = $db->prepare('INSERT INTO Users (username, email, password) VALUES (:username, :email, :password)');
        $stmt->bindValue(':username', $username, SQLITE3_TEXT);
        $stmt->bindValue(':email', $email, SQLITE3_TEXT);
        $stmt->bindValue(':password', secure_password_hash($password), SQLITE3_TEXT);

        $result = $stmt->execute();

        if ($result) {
            echo 'Registration successful';
        } else {
            echo 'Registration failed';
        }
    }

    // Close database connection
    $db->close();
}
?>

<!-- Registration form -->
<form method="POST">
    <input type="hidden" name="token" value="<?php echo $_SESSION['token']; ?>" />

    <label>Username:</label>
    <input type="text" name="username"><br>
    <label>Email:</label>
    <input type="email" name="email"><br>
    <label>Password:</label>
    <input type="password" name="password"><br>

    <input type="submit" value="Register">
</form>
