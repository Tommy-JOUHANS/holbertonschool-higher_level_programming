#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const secondBig = process.argv.slice(2).map(Number).sort((a, b) => b - a);
  console.log(secondBig[1]);
}
