#!/usr/bin/node

const args = process.argv.slice(2);
const nums = args.map(Number);

if (nums.length < 2) {
  console.log('0');
} else {
  let biggest = 0;
  let second = -Infinity;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > nums[biggest]) {
      biggest = i;
    }
  }
  for (let j = 0; j < nums.length; j++) {
    if (nums[j] > second && j !== biggest) {
      second = nums[j];
    }
  }
  console.log(`${second}`);
}
