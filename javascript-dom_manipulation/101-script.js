#!/usr/bin/node
document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('btn_translate').addEventListener('click', function () {
    const languageCode = document.getElementById('language_code').value;

    if (!languageCode) {
      document.getElementById('hello').textContent = 'Please select a language.';
      return;
    }

    fetch(`https://hellosalut.stefanbohacek.com/?lang=${languageCode}`)
      .then(response => response.json())
      .then(data => {
        document.getElementById('hello').textContent = data.hello;
      })
      .catch(() => {
        document.getElementById('hello').textContent = 'Error fetching translation.';
      });
  });
});
