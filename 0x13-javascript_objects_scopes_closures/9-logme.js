#!/usr/bin/node
/**
 * The function that prints the number of arguments already printed 
 * and the new argument value.
 */

let printedCount = 0;

exports.logMe = function (item) {
    console.log(printedCount + ': ' + item);
    printedCount++;
};
