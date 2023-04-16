<?php

require('includes/init.php');

check_user_logged_in();

?>
<!DOCTYPE HTML>
<html lang="en">
    <head>

        <title>Homepage ~ DataDown</title>

        <link rel="stylesheet" href="css/styles.css" media="all" type="text/css"/>

        <!-- Font -->
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
              rel="stylesheet"
              crossorigin="anonymous"
              referrerpolicy="no-referrer"/>

        <!-- MDB framework -->
        <link rel="stylesheet"
              href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.2.0/mdb.dark.min.css"
              integrity="sha512-TwhKh1HgMAOxx1412XkhJwdQkaRnRTzFsmJkMeT9YJkTrFvpgfiu51fccoNtalKoeN9X5YSgUynDbOlHAxT72A=="
              crossorigin="anonymous"
              referrerpolicy="no-referrer"/>

    </head>
    <body>

        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <a class="px-3 navbar-brand" href="#">Clam-Corp Data Portal</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">System Status</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Mail Client</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Intranet</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Access Records</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="?">User Profile</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/logout.php">Logout</a>
                    </li>
                </ul>
            </div>
        </nav>

        <div class="container my-5">
            <div class="row">
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">User Info</h5>
                            <p class="card-text">
                                <strong>Name:</strong> <?php echo $_SESSION['first_name'] . ' ' . $_SESSION['last_name']; ?>
                            </p>
                            <p class="card-text">
                                <strong>Gender:</strong> <?php echo $_SESSION['gender']; ?>
                            </p>
                            <p class="card-text">
                                <strong>System Role:</strong> <?php echo $_SESSION['role']; ?>
                            </p>
                            <p class="card-text">
                                <strong>Email:</strong> <?php echo $_SESSION['email']; ?>
                            </p>
                            <p class="card-text">
                                <?php
                                if ($_SESSION['username'] === 'admin') {
                                    echo 'Flag: ' . file_get_contents('/flag.txt');
                                }
                                ?>
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-8">
                    <div class="card">
                        <div class="card-body text-light">
                            <h5 class="card-title">Recent Activity</h5>
                            <ul class="list-group">
                                <li class="list-group-item text-light">Signed up for the service</li>
                                <li class="list-group-item text-light">Updated profile information</li>
                                <li class="list-group-item text-light">Posted a comment</li>
                                <li class="list-group-item text-light">Liked a post</li>
                                <li class="list-group-item text-light">Followed a user</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.2.0/mdb.min.js"
                integrity="sha512-ec1IDrAZxPSKIe2wZpNhxoFIDjmqJ+Z5SGhbuXZrw+VheJu2MqqJfnYsCD8rf71sQfKYMF4JxNSnKCjDCZ/Hlw=="
                crossorigin="anonymous"
                referrerpolicy="no-referrer"></script>
    </body>
</html>
