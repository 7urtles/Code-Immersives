const http = require('http');
const fs = require('fs')

const express = require('express');
const app = express();


const hostname = '0.0.0.0';
const port = 80;

app.use(express.static('static'));

app.use('/', express.static('static'));

app.listen(port, () => console.log(`listening on port ${port}!`));