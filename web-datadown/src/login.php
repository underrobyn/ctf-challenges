<?php

require('includes/init.php');

check_user_anonymous();

$errors = '';

// Get login form data
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (empty($_POST['username']) or empty($_POST['password'])) {
        $errors = 'Please enter both a username and a password!';
    } else {
        $username = $_POST['username'];
        $password = $_POST['password'];

        // Connect to database
        $dbm = new database();
        $db = $dbm->getInstance();

        // Check if user exists and password matches
        $stmt = $db->prepare('SELECT password FROM Users WHERE username = :username');
        $stmt->bindValue(':username', $username, SQLITE3_TEXT);

        $result = $stmt->execute();
        $row = $result->fetchArray(SQLITE3_ASSOC);

        if ($row && secure_password_verify($password, $row['password'])) {
            // Login successful
            echo 'Welcome, ' . $username . '!';
            $_SESSION['logged_in'] = true;
            $_SESSION['username'] = $username;
            redirect('/index.php');
        } else {
            $errors = 'Invalid username or password!';
        }

        // Close database connection
        $db->close();
    }
}
?>
<!DOCTYPE HTML>
<html lang="en">
    <head>

        <title>Login ~ DataDown</title>

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

                                    <h2 class="fw-bold mb-2 text-uppercase">Login</h2>
                                    <p class="text-white-50 mb-5">Please enter your login and password!</p>

                                    <?php
                                    if ($errors !== '') {
                                        echo "<div class='alert alert-danger' role='alert'>{$errors}</div>";
                                    }
                                    ?>

                                    <form method="POST" action="login.php">
                                        <input type="hidden" name="token" value="<?php echo $_SESSION['token']; ?>" />

                                        <div class="form-outline form-white mb-4">
                                            <input type="text" id="username" name="username" class="form-control form-control-lg" />
                                            <label class="form-label" for="username">Username</label>
                                        </div>

                                        <div class="form-outline form-white mb-4">
                                            <input type="password" id="password" name="password" class="form-control form-control-lg" />
                                            <label class="form-label" for="password">Password</label>
                                        </div>

                                        <button class="btn btn-outline-light btn-lg px-5" type="submit">Login</button>
                                    </form>

                                </div>

                                <div>
                                    <p class="mb-0">
                                        Don't have an account? <a href="/register.php" class="text-white-50 fw-bold">Register here</a>
                                    </p>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.2.0/mdb.min.js"
                integrity="sha512-ec1IDrAZxPSKIe2wZpNhxoFIDjmqJ+Z5SGhbuXZrw+VheJu2MqqJfnYsCD8rf71sQfKYMF4JxNSnKCjDCZ/Hlw=="
                crossorigin="anonymous"
                referrerpolicy="no-referrer"></script>

    </body>
</html>
