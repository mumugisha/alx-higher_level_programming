#!/usr/bin/node
/**
 * The function that returns the reversed version of a list
 */

const esrever = (list) => {
  const revArray = [];
  list.forEach((component) => revArray.unshift(component));
  return revArray;
};

module.exports = { esrever };
