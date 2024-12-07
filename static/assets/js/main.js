document
    .querySelector(".dropdown-toggle")
    .addEventListener("click", function () {
        const menu = document.querySelector(".menu");
        menu.classList.toggle("show");
    });

const cartButton = document.getElementById("shopping-cart-btn");
const cartMenu = document.getElementById("shopping-cart-menu");
const closeCartButton = document.getElementById("close-cart-menu");

cartButton.addEventListener("click", () => {
    cartMenu.classList.toggle("hidden"); // Show or hide the cart menu
});

// Function to close the cart menu
closeCartButton.addEventListener("click", () => {
    cartMenu.classList.add("hidden"); // Hide the cart menu
});

// Close cart menu if the user clicks outside it
window.addEventListener("click", (e) => {
    if (!cartMenu.contains(e.target) && e.target !== cartButton) {
        cartMenu.classList.add("hidden");
    }
});
