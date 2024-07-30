#!/usr/bin/node

// Write a script that gets the contents of a
// webpage and stores it in a file.

const request = require('request');
const { writeFile } = require('fs');
const argv = process.argv;

request(argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    writeFile(argv[3], body, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
