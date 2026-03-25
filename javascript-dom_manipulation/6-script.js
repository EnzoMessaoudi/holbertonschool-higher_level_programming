const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

const characterDiv = document.getElementById('character');

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not OK');
    }
    return response.json();
  })
  .then(data => {
    characterDiv.textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching character:', error);
    characterDiv.textContent = 'Failed to load character';
  });
