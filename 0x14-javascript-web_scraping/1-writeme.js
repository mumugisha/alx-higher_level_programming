#!/usr/bin/node


// Write a script that writes a string to a file


const fs = require('fs');
const filePath = process.argv[2];
const stringWrite = process.argv[3];


// Write files using Js
fs.writeFile(filePath, stringWrite, 'utf-8', (err) => {
  if (error) {
      return console.log(error);
  }
});
