#!/usr/bin/node

// Write a script that displays the status code of a GET request

const request = require('request');
const argv = process.argv;

request(argv[2], (err, response) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  console.log('code:', response && response.statusCode);
});
