#!/usr/bin/node

if (process.argv.length > 3) {
  const args = process.argv.slice(2).map(Number);
  args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
} else {
  console.log(0);
}
