const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

const movies = document.getElementById('list_movies');

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not OK');
    }
    return response.json();
  })
  .then(data => {
    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      movies.appendChild(li);
    });
  })
  .catch(error => {
    console.error('Error fetching character:', error);
    movies.textContent = 'Failed to load movies';
  });
