const express        = require('express');
const router         = express.Router({caseSensitive: true});
let db;

const jwt = require("jsonwebtoken");


router.post('/login', (req, res) => {
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

router.get('/users', (req, res) => {
    const token = req.headers.authorization.split(' ')[1];

    try {
        const payload = jwt.decode(token);
        res.json({ username: payload.username, role: payload.role });
    } catch (error) {
        res.status(401).json({ error: 'Invalid token' });
    }
});

router.get('/login', (req, res) => {
    res.render('login.html');
});

router.get('/register', (req, res) => {
    res.render('register.html');
});

router.post('/register', (req, res) => {
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
