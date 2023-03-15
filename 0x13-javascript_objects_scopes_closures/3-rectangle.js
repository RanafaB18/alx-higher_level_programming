#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let output = '';
    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        output += 'X';
      }
      output += '\n';
    }
    output = output.substring(0, output.length - 1);
    console.log(output);
  }
}
module.exports = Rectangle;
