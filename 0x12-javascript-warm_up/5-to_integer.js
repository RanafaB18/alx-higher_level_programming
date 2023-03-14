#!/usr/bin/node

first = Number(process.argv[2]);
const output =  isNaN(first) ? 'Not a number' : `My number: ${Math.floor(first)}`;
console.log(output)
