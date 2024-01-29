const header = document.querySelector("#red_header");
header.addEventListener("click", addclass);

function addclass() {
  const redelement = document.querySelector("redelement");
  redelement.classList.add("red");
}
