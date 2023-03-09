<?php

require('includes/init.php');

check_user_logged_in();

echo 'You are logged in as: ' . $_SESSION['username'];

phpinfo();
