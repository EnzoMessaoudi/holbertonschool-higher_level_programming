#!/usr/bin/node

function add (a, b) {
  const res = Number(a) + Number(b);
  console.log(`${res}`);
}

const args = process.argv.slice(2);

if (isNaN(args[0]) || isNaN(args[1])) {
  console.log('NaN');
} else {
  add(args[0], args[1]);
}
