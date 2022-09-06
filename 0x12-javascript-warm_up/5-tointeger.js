#!/usr/bin/node
const argConvert = parseInt(process.argv[2]);
if (isNaN(argConvert)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argConvert);
}
