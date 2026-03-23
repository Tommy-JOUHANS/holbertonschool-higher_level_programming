#!/usr/bin/node
fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
  .then(response => response.json())
  .then(data => {
    const helloSay = document.getElementById('hello');
    helloSay.textContent = data.hello;
  });
