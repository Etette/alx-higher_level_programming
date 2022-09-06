#!/usr/bin/node
const arg = process.argv.slice(2).map((x) => {
  return parseInt(x);
});

if (arg.length <= 1) {
  console.log(0);
} else {
  console.log(arg.sort((a, b) => {
    return b - a;
  })[1]);
}
