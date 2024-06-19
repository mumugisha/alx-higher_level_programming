#!/usr/bin/node

const { argv } = require('process');

function factorial (number) {
  if (number <= 1) return 1;
  
  return factorial(number - 1) * number;
}

const recursev = parseInt(argv[2]);
console.log(isNaN(recursev) ? 1 : factorial(recursev));
