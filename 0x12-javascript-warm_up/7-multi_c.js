#!/usr/bin/node

const first = Number(process.argv[2]);
if (isNaN(first)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < first; i++) {
    console.log('C is fun');
  }
}
