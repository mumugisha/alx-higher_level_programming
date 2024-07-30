#!/usr/bin/node

// Write a script that reads and prints the content of a file

const fs = require('fs');
const filepath = process.argv[2];

// read files using Js
fs.readFile(filepath, { encoding: 'utf8' }, (err, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(content);
  }
});
