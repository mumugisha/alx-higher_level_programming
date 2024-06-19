#!/usr/bin/node
/**
 * Script that imports an array from a file and computes a new array.
 * The script imports list from the file 100-data.js.
 *
 * The new array is created with each value being the product of the
 * initial list value and its index.
 */
const { list } = require('./100-data.js');

console.log(list);
const newArray = list.map((value, index) => value * index);
console.log(newArray);
