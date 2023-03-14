#!/usr/bin/node

let first = Number(process.argv[2]);
if (isNaN(first)) {
  first = 1;
}
function factorial (num) {
  if (num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(first));
