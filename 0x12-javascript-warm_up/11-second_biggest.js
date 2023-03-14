#!/usr/bin/node

const numOfArgs = process.argv.length;
if (numOfArgs === 2 || numOfArgs === 3) {
  console.log(0);
} else {
  let maximum = Number(process.argv[2]);
  let prevMaximum = 0
  for (let index = 2; index < numOfArgs; index++) {
    const current = Number(process.argv[index]);
    if (current > maximum) {
      prevMaximum = maximum
      maximum = current;
    }
  }
  console.log(prevMaximum);
}
