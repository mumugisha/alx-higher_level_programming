#!/usr/bin/node
/**
 * Defining a rectangle class using notation
 * The constructor must take 2 arguments: w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * If w or h is equal to 0 or not a positive integer, create an empty object
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  /**
 * Create an instance method called print()
 * prints the rectangle using the character X
 */

  print () {
    for (let a = 0; a < this.height; a++) {
      console.log('X'.repeat(this.width));
    }
  }
  /**
 * Create an instance method called rotate()
 * Exchanges the width and the height of the rectangle
 */

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  /**
 * Create an instance method called double()
 * Multiples the width and the height of the rectangle by 2
 */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
