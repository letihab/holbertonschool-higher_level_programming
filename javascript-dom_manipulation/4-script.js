const lielement = document.querySelector("#add_item");
lielement.addEventListener("click", newElement);

function newElement() {
  const newLi = document.createElement("li");
  newLI.textContent = "Item";
  const mylistElement = document.querySelector(".my_list");
  mylistElement.appendChild(newLi);
}
