document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const helloElement = document.getElementById('hello');

  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not OK');
      }
      return response.json();
    })
    .then(data => {
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching hello:', error);
      helloElement.textContent = 'Failed to load greeting';
    });
});
