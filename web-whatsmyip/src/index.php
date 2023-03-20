<?php

function get_real_user_ip() {
    // Credit to: https://stackoverflow.com/a/55790
    $ip = $_SERVER['REMOTE_ADDR'];

    if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
        $ip = $_SERVER['HTTP_CLIENT_IP'];
    } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    }

    return $ip;
}


$user_ip = get_real_user_ip();

// If user's IP is invalid then we send HTTP 400 (Bad Request)
if (!filter_var($user_ip, FILTER_VALIDATE_IP)) {
    http_response_code(400);
    die();
}


// If user's IP is not in a private range, then this is an external request
$is_external = true;
if (!filter_var($user_ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE)) {
    $is_external = false;
}


// Load the flag
$real_flag = trim(file_get_contents('/flag.txt'));

// Start constructing the response
$r = array(
    'ip' => $user_ip,
    'time' => time(),
    'flag' => ''
);

if ($is_external === false) {
    $r['flag'] = $real_flag;
}

header('Content-Type: application/json');
die(json_encode($r, JSON_PRETTY_PRINT));
