// Call `fetch()`, passing in the URL.
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then((response) => {
    if (response.ok) {
      throw response.json();
    } else {
        // Handle the error if the request was not successful
        throw new Error("Failed to fetch character data");
    }
   })
   .then(data => {
    const characterElement = document.getElementById("character");
    characterElement.textContent = data.name;
   })
   .catch(error => {
    // Log and handle any errors that occurred during the fetch
    console.error("Error:", error.message);
  });
