#!/usr/bin/node

const { argv } = require('process');

if (argv[2] === undefined) {
  console.log('No argument');
} else if (argv[3] === undefined) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
