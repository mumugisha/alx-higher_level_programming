#!/usr/bin/node
/**
 * Defining a rectangle class using notation and extends
 */
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {

    constructor(size) {
        super(size, size);
    }
}

module.exports = Square;
