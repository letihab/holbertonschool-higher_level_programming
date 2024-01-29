const header = document.querySelector("header");
header.addEventListener("click", addclass);

function addclass() {
  const redelement = document.querySelector("header");
  redelement.classList.add("red");
}
