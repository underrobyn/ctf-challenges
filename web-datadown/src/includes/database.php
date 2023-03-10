<?php

class DatabaseManager
{

    protected string $database_file = 'users.db';
    protected string $database_path = '/var/www/html/';

    private SQLite3 $instance;

    public function __construct() {
        $full_path = $this->database_path . $this->database_file;

        $this->instance = new SQLite3($full_path);

        return $this;
    }

    public function getInstance() {
        return $this->instance;
    }

}
