#!/usr/bin/node

const numOfArgs = process.argv.length;
console.log(numOfArgs === 3 ? 'Argument found' : numOfArgs === 2 ? 'No argument' : 'Arguments found');
