#!/usr/bin/node

// Script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const request = require('request');
const argv = process.argv;
const requestUrl = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request(requestUrl, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
