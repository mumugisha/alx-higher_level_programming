#!/usr/bin/node

const X = process.argv[2];

if (!parseInt(X)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < parseInt(X); a++) {
    let b = 0;
    let size = '';

    while (b < parseInt(X)) {
      size += 'X';
      b++;
    }
    console.log(size);
  }
}
