<?php

require('includes/init.php');

check_user_logged_in();

?>
<!DOCTYPE HTML>
<html lang="en">
    <head>

        <title>Homepage ~ DataDown</title>

        <link rel="stylesheet" href="css/styles.css" media="all" type="text/css" />

        <!-- Font -->
        <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
              rel="stylesheet"
              crossorigin="anonymous"
              referrerpolicy="no-referrer" />

        <!-- MDB framework -->
        <link rel="stylesheet"
              href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.2.0/mdb.dark.min.css"
              integrity="sha512-TwhKh1HgMAOxx1412XkhJwdQkaRnRTzFsmJkMeT9YJkTrFvpgfiu51fccoNtalKoeN9X5YSgUynDbOlHAxT72A=="
              crossorigin="anonymous"
              referrerpolicy="no-referrer" />

    </head>
    <body>
        <?php
            echo 'You are logged in as: ' . $_SESSION['username'] . '<br />';
            if ($_SESSION['username'] === 'admin') {
                echo file_get_contents('/flag.txt');
            }
            session_destroy();
        ?>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.2.0/mdb.min.js"
                integrity="sha512-ec1IDrAZxPSKIe2wZpNhxoFIDjmqJ+Z5SGhbuXZrw+VheJu2MqqJfnYsCD8rf71sQfKYMF4JxNSnKCjDCZ/Hlw=="
                crossorigin="anonymous"
                referrerpolicy="no-referrer"></script>
    </body>
</html>
