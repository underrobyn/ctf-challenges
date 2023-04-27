const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const nunjucks = require('nunjucks');
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

nunjucks.configure('views', { // Configure Nunjucks
  autoescape: true,
  express: app,
});

let users = [];
const secretKey = 'insecure_secret_key';



app.listen(3000, () => {
    console.log('Server running on port 3000');
});
