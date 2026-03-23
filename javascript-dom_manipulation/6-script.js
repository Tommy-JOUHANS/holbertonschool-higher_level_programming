#!/usr/bin/node
document.addEventListener('DOMContentLoaded', async function () {
  const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const data = await response.json();
  document.getElementById('character').textContent = data.name;
});
