const express = require('express');
const path = require('path');
const app = express();
const port = 3440;

app.get('/', (req,res) => {
    res.send("Hello the Express server is Running on port 3440!!")
});

app.listen(port, () => {
    console.log("The Express app is running in PORT:3440")
});