const carouselImages = document.querySelector(".carousel-images");
const images = document.querySelectorAll(".carousel-images img");
const prevButton = document.querySelector(".prev-btn");
const nextButton = document.querySelector(".next-btn");
const originalPrice = document.querySelector(".original-price");
const discountedPrice = document.querySelector(".discounted-price");

originalPrice.textContent = "$29.99";
discountedPrice.textContent = "$24.99";

let currentIndex = 0;

function updateCarousel() {
    const offset = -currentIndex * 100;
    carouselImages.style.transform = `translateX(${offset}%)`;
}

prevButton.addEventListener("click", () => {
    currentIndex = currentIndex > 0 ? currentIndex - 1 : images.length - 1;
    updateCarousel();
});

nextButton.addEventListener("click", () => {
    currentIndex = currentIndex < images.length - 1 ? currentIndex + 1 : 0;
    updateCarousel();
});
