#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2 || args.length === 1) {
  console.log('0');
} else {
  let biggest = 0;
  let second = -Infinity;
  for (let i = 0; i < args.length; i++) {
    if (args[i] > args[biggest]) {
      biggest = i;
    }
  }
  for (let j = 0; j < args.length; j++) {
    if (args[j] > second && j !== biggest) {
      second = args[j];
    }
  }
  console.log(`${second}`);
}
