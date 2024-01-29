const header = document.querySelector("#red_header");
header.addEventListener("click", addClass);

function addClass() {
  const headerElement = document.querySelector("header");
  headerElement.classList.add("red");
}
