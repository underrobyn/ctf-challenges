const express = require('express');
const jwt = require('jsonwebtoken');
const app = express();

app.use(express.json());

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

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
