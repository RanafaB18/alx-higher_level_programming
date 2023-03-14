#!/usr/bin/node

const first = process.argv[2];
let output = '';
if (isNaN(first)) {
  console.log('Missing size');
} else {
  for (let vertical = 0; vertical < first; vertical++) {
    for (let horizon = 0; horizon < first; horizon++) {
      output += 'X';
    }
    output += '\n';
  }
  output = output.substring(0, output.length - 1);
  console.log(output);
}
