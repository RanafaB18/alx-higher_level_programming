#!/usr/bin/node

const Rectangle = require('./0-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
