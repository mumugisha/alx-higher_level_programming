#!/usr/bin/node
/**
 * Defining a rectangle class using notation and extends
 */
const Squared = require('./5-square.js');

class Square extends Squared {
    /**
     * Create an instance method called charPrint(c)
     * Print the rectangle using the character c
     * If c is undefined, use the character X
     */
    charPrint(c) {
        if (c === undefined) {
            c = 'X'; 
        }
        for (let a = 0; a < this.height; a++) {
            let s = '';
            for (let b = 0; b < this.width; b++) {
                s += c;
            }
            console.log(s);
        }
    }
}

module.exports = Square;
