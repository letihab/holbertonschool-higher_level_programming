const header = document.querySelector("#red_header");
header.addEventListener("click", red_header);

function red_header() {
  const headerelement = document.querySelector("header");
  headerelement.style.color = "#FF0000";
}
