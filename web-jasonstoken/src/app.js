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

app.post('/login', (req, res) => {
    const { username, password } = req.body;

    if (username === 'admin' && password === 'password') {
        const payload = {
            username: 'admin',
            role: 'admin'
        };

        const token = jwt.sign(payload, secretKey);
        res.json({ token });
    } else {
        res.status(401).json({ error: 'Invalid username or password' });
    }
});

app.get('/users', (req, res) => {
    const token = req.headers.authorization.split(' ')[1];

    try {
        const payload = jwt.decode(token);
        res.json({ username: payload.username, role: payload.role });
    } catch (error) {
        res.status(401).json({ error: 'Invalid token' });
    }
});

app.get('/login', (req, res) => {
  res.render('login.html');
});

app.get('/register', (req, res) => {
  res.render('register.html');
});

app.post('/register', (req, res) => {
  const { username, password } = req.body;

  const userExists = users.find((user) => user.username === username);

  if (userExists) return res.status(400).send('User already exists.');

  const hashedPassword = bcrypt.hashSync(password, 10);
  const newUser = {
    id: users.length + 1,
    username,
    password: hashedPassword,
  };

  users.push(newUser);

  res.status(201).send('User created.');
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
