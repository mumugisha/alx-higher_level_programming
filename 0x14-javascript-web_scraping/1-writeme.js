#!/usr/bin/node

// Write a script that writes a string to a file

const fs = require('fs');

const filePath = process.argv[2];
const fileWrite = process.argv[3];

// Write files using Js
fs.writeFile(filePath, fileWrite, { encoding: 'utf8' }, (err) => {
  if (err) {
    console.log(err);
  } else {
    console.log('File written successfully');
  }
});
