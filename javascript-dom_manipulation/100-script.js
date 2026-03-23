#!/usr/bin/node
document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('add_item').addEventListener('click', function () {
    const list = document.querySelector('.my_list');
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
  });

  document.getElementById('remove_item').addEventListener('click', function () {
    const list = document.querySelector('.my_list');
    if (list.lastElementChild) {
      list.removeChild(list.lastElementChild);
    }
  });

  document.getElementById('clear_list').addEventListener('click', function () {
    const list = document.querySelector('.my_list');
    list.innerHTML = '';
  });
});
