#!/usr/bin/node
document.getElementById('add_item').addEventListener('click', function () {
  const myList = document.querySelector('.my_list');
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  myList.appendChild(newItem);
});
