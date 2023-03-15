#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let fmt = 'C';
    let output = '';
    if (!c) {
      fmt = 'X';
    }
    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        output += fmt;
      }
      output += '\n';
    }
    output = output.substring(0, output.length - 1);
    console.log(output);
  }
}

module.exports = Square;
