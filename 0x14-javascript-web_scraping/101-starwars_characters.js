#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function printCharacters(chars, idx) {
  request(chars[idx], (err, res, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < chars.length) printCharacters(chars, idx + 1);
    }
  });
}

request(url, (err, res, body) => {
  if (!err) printCharacters(JSON.parse(body).characters, 0);
});
