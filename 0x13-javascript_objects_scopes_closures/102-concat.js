#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: node concat-files.js <file1> <file2> <destination>');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (!fs.existsSync(fileA) || !fs.existsSync(fileB) || !fs.statSync(fileA).isFile() || !fs.statSync(fileB).isFile()) {
  console.error('Error: File 1 and File 2 must exist and be valid files');
  process.exit(1);
}

const fileAdata = fs.readFileSync(fileA);
const fileBdata = fs.readFileSync(fileB);
const concatenatedData = Buffer.concat([fileAdata, fileBdata]);

fs.writeFileSync(fileC, concatenatedData);

console.log(`Concatenated ${fileA} and ${fileB} into ${fileC}`);
