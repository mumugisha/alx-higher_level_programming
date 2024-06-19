#!/usr/bin/node

function add(a, b) {
  return a + b;
}

const { argv } = require('process');
const abc1 = parseInt(argv[2]);
const abc2 = parseInt(argv[3]);

console.log(add(abc1, abc2));
