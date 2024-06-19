#!/usr/bin/node

const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let a = 0; a < parseInt(x); a++) {
    console.log('C is fun');
  }
}
