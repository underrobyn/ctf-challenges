<?php

function secure_password_hash($password) {
    // TODO: Implement this
    return $password;
}

function secure_password_verify($password, $hash) {
    // TODO: Implement this
    return $password === $hash;
}

function get_random_str($bytes = 10) {
    return bin2hex(random_bytes($bytes));
}

function redirect($url) {
    header("Location: {$url}");
    die ("<script>window.location.href='{$url}';</script>Redirecting you to {$url}");
}

function check_user_logged_in() {
    // If not logged in, redirect to login page
    if (!$_SESSION['logged_in'] === true) {
        redirect('/login.php');
    }
}

function check_user_anonymous() {
    if ($_SESSION['logged_in'] === true) {
        redirect('/index.php');
    }
}

// Create HTTP session
session_name("__rctf_datadown_session");
session_set_cookie_params(86400, '/', null, false, true); // Set secure=false due to no HTTPS
@session_start(); // Ignore any session start errors

if (!isset($_SESSION['start'])) {
    $_SESSION['start'] = time();
    $_SESSION['logged_in'] = false;
    $_SESSION['token'] = get_random_str(16);
}