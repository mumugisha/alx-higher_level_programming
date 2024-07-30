#!/usr/bin/node

// Write a script that display the status code of a GET request

const request = require('request');
const requestUrl = process.argv[2];

request(requestUrl, (err, response) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  console.log('code:', response && response.statusCode);
});
