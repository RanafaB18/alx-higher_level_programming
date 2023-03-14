#!/usr/bin/node

const numOfArgs = process.argv.length;
if (numOfArgs === 2 || numOfArgs === 3) {
  console.log(1);
} else {
  let maximum = Number(process.argv[2]);
  for (let index = 3; index < numOfArgs; index++) {
    const current = Number(process.argv[index]);
    if (current > maximum) {
      maximum = current;
    }
  }
  console.log(maximum);
}
