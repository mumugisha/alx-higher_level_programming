#!/usr/bin/node

const { argv } = require('process');
const numb = parseInt(argv[2]);

console.log(Number.isInteger(numb) ? `My number: ${numb}` : 'Not a Number');
