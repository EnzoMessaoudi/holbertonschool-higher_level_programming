const header = document.querySelector('header');

const link = document.querySelector('#red_header');
link.addEventListener('click', () => {
  header.classList.add('red');
});
