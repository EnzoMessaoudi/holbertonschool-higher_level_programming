const header = document.querySelector('header');

const button = document.querySelector('#update_header');
button.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
