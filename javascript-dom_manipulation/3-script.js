const toggleheaderelement = document.querySelector("#toggle_header");
toggleheaderelement.addEventListener("click", reverseColor);

function reverseColor() {
  const headerElement = document.querySelector("header");
    if (headerElement.classList.contains("red")) {
      headerElement.classList.remove("red");
      headerElement.classList.add("green");
    } else if (headerElement.classList.contains("green")) {
      headerElement.classList.remove("green");
      headerElement.classList.add("red"); 
    } else {
      headerElement.classList.add("red");
    }
}
