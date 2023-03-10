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
<!DOCTYPE HTML>
<html lang="en">
    <head>

        <title>Register ~ DataDown</title>

        <link rel="stylesheet" href="css/styles.css" media="all" type="text/css" />

        <!-- Font -->
        <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
              rel="stylesheet"
              crossorigin="anonymous"
              referrerpolicy="no-referrer" />

        <!-- MDB framework -->
        <link rel="stylesheet"
              href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.2.0/mdb.min.css"
              integrity="sha512-9oXHUIbY5ggztQSpGM/F8ffumz2nTHkG81Qxvm/JJOlcj0nPu8T/A/vCXmlJRP2wt4iF3L2zL+P1rF2odicJ3Q=="
              crossorigin="anonymous"
              referrerpolicy="no-referrer" />

    </head>
    <body>

        <section class="vh-100 gradient-custom">
            <div class="container py-5 h-100">
                <div class="row d-flex justify-content-center align-items-center h-100">
                    <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                        <div class="card bg-dark text-white" style="border-radius: 1rem;">
                            <div class="card-body p-5 text-center">

                                <div class="mb-md-5 mt-md-4 pb-5">

                                    <h2 class="fw-bold mb-2 text-uppercase">Register</h2>
                                    <p class="text-white-50 mb-5">Please use the form below to create an account:</p>

                                    <form method="POST" action="/register.php">
                                        <input type="hidden" name="token" value="<?php echo $_SESSION['token']; ?>" />

                                        <div class="form-outline form-white mb-4">
                                            <input type="text" id="username" class="form-control form-control-lg" />
                                            <label class="form-label" for="username">Username</label>
                                        </div>

                                        <div class="form-outline form-white mb-4">
                                            <input type="email" id="email" class="form-control form-control-lg" />
                                            <label class="form-label" for="email">Email</label>
                                        </div>

                                        <div class="form-outline form-white mb-4">
                                            <input type="password" id="password" name="password" class="form-control form-control-lg" />
                                            <label class="form-label" for="password">Password</label>
                                        </div>

                                        <button class="btn btn-outline-light btn-lg px-5" type="submit">Register</button>

                                    </form>

                                </div>

                                <div>
                                    <p class="mb-0">
                                        Already have an account? <a href="/login.php" class="text-white-50 fw-bold">Login here</a>
                                    </p>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </body>
</html>
