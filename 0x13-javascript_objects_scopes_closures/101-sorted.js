#!/usr/bin/node
/**
 * The script that imports a dictionary of occurrences by user id
 * And computes a dictionary of user ids by occurrence
 * The script must import dict from the file 101-data.js
 */

const { dict } = require('./101-data.js');

const newDict = {};

Object.entries(dict).forEach(([userId, occurrences]) => {
  if (newDict[occurrences]) {
    newDict[occurrences].push(userId);
  } else {
    newDict[occurrences] = [userId];
  }
});

console.log(newDict);
