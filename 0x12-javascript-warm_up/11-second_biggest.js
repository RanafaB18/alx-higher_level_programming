#!/usr/bin/node

const numOfArgs = process.argv.length;
if (numOfArgs === 2 || numOfArgs === 3) {
  console.log(0);
} else {
    const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
    console.log(args[args.length - 2])
}
