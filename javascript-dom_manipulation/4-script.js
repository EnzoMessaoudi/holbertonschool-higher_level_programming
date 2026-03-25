const list = document.querySelector('.my_list');
const button = document.querySelector('#add_item');
button.addEventListener('click', () => {
    const li = document.createElement('li');
    li.textContent = 'Item';
    list.appendChild(li);
});
