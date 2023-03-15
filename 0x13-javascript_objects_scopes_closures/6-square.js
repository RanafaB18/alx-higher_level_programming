#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let output = '';
    if (c === undefined) {
      this.print();
    } else {
      for (let y = 0; y < this.height; y++) {
        for (let x = 0; x < this.width; x++) {
          output += 'C';
        }
        output += '\n';
      }
      output = output.substring(0, output.length - 1);
      console.log(output);
    }
  }
}

module.exports = Square;
