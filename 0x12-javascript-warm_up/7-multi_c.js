#!/usr/bin/node
const numTimes = parseInt(process.argv[2]);
if (isNaN(numTimes) || numTimes === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numTimes.length; i++) {
    console.log('C is fun');
  }
}
