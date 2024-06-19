#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const { argv } = require('process');
const number1 = parseInt(argv[2], 10);
const number2 = parseInt(argv[3], 10);

console.log(add(number1, number2));
