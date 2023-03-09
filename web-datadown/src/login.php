<?php

require('includes/init.php');

check_user_anonymous();

// SQLite database file path
$db_file = 'users.db';

// Get login form data
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Connect to database
    $db = new SQLite3($db_file);

    // Check if user exists and password matches
    $stmt = $db->prepare('SELECT password FROM Users WHERE username = :username');
    $stmt->bindValue(':username', $username, SQLITE3_TEXT);

    $result = $stmt->execute();
    $row = $result->fetchArray(SQLITE3_ASSOC);

    if ($row && secure_password_verify($password, $row['password'])) {
        // Login successful
        echo 'Welcome, '.$username.'!';
        $_SESSION['logged_in'] = true;
        $_SESSION['username'] = $username;
        redirect('/index.php');
    } else {
        // Login failed
        echo 'Invalid username or password';
    }

    // Close database connection
    $db->close();
}
?>

<!-- Login form -->
<form method="POST">
    <input type="hidden" name="token" value="<?php echo $_SESSION['token']; ?>" />

    <label>Username:</label>
    <input type="text" name="username"><br>
    <label>Password:</label>
    <input type="password" name="password"><br>

    <input type="submit" value="Login">
</form>
