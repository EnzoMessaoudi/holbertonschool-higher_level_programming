#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 1 || args.length === 1) {
  console.log('0');
} else {
  let biggest = args[0];
  let second = args[0];
  for (let i = 0; i < args.length; i++) {
    if (args[i] > biggest) {
      biggest = args[i];
    }
  }
  for (let j = 0; j < args.length; j++) {
    if (args[j] > second && args[j] !== biggest) {
      second = args[j];
    }
  }
  console.log(`${second}`);
}
