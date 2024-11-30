document
  .querySelector(".dropdown-toggle")
  .addEventListener("click", function () {
    const menu = document.querySelector(".menu");
    menu.classList.toggle("show");
  });
