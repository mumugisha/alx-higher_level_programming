#!/usr/bin/node

// Write a script that prints all characters of a Star Wars movie:

var request = require('request');
var url = 'https://swapi-api.alx-tools.com/api/films/' + args()[0];

function printCharacters (chars, idx) {
  request(chars[idx], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < chars.length) {
        printCharacters(chars, idx + 1);
      }
    }
  });
}

function varName () {
  return 'value';
}

function args () {
  return process.argv.slice(2);
}

// Call varName to avoid no-unused-vars error
varName();

request(url, function (err, res, body) {
  if (!err) {
    printCharacters(JSON.parse(body).characters, 0);
  }
});
