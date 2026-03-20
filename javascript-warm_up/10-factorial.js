#!/usr/bin/node

const args = process.argv.slice(2);

function factorial (a) {
  if (a <= 1) {
    return a;
  }
  return a * factorial(a - 1);
}

if (isNaN(args[0])) {
  console.log('NaN');
} else {
  const res = factorial(args[0]);
  console.log(`${res}`);
}
