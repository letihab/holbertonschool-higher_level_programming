fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
  .then(response => response.json())
  .then(hello => displayHello(hello));

function displayHello(hello) {
    const divhello = document.querySelector("#hello");
    divhello.textContent = hello.hello;
}
