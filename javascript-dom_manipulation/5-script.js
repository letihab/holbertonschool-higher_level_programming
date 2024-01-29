const headerElement = document.querySelector("#update_header");
headerElement.addEventListener("click", updateText);

function updateText () {
  const newheaderElement = document.querySelector("header");
  newheaderElement.textContent = "New Header!!!"
}
