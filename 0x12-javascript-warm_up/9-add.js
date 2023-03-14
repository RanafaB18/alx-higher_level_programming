#!/usr/bin/node

const first = Number(process.argv[2]);
const second = Number(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(first, second));
