#!/usr/bin/node

const x = parseInt(process.argv[2], 10);

if (isNaN(x)) {
  console.log('Missing size');
} else if (x > 0) {
  const square = 'X'.repeat(x);
  for (let i = 0; i < x; i++) {
    console.log(square);
  }
}
