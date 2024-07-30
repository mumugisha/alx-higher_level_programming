#!/usr/bin/node

// Write a script that writes a string to a file

const fs = require('fs');

const filepath = process.argv[2];
const fileWrite = process.argv[3];

// Write files using Js
fs.writeFile(filepath, fileWrite, { encoding: 'utf8' }, (err) => {
  if (err) {
	  return console.log(err);
  } else {
	  return console.log('File written successfully');
  }
});
