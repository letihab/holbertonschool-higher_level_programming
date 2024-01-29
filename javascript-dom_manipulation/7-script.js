// Wait for the HTML document to be fully loaded before manipulating it
document.addEventListener("DOMContentLoaded", function () {
    // Use the Fetch API to fetch the movie data from the URL
    fetch("https://swapi-api.hbtn.io/api/films/?format=json")
      .then(response => response.json())
      .then(movies => showMovieTitles(movies.results)) // Fixed typo in 'results' property
  
    function showMovieTitles(movieData) {
      // Select the HTML ul element with id "list_movies"
      var listMoviesElement = document.getElementById("list_movies");
  
      // Loop through each movie and add its title to the list
      movieData.forEach(movie => {
        // Create a new li element
        var newLiElement = document.createElement("li");
  
        // Set the text content of the new li element to the movie title
        newLiElement.textContent = movie.title;
  
        // Append the new li element to the ul
        listMoviesElement.appendChild(newLiElement);
      });
    }
  });
  