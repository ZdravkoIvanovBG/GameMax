async function fetchGameData(franchise = null) {
    try {
        let apiURL = 'api/games/';

        if (franchise) {
            apiURL += `?franchise=${franchise}`;
        }

        const response = await fetch(apiURL);

        if (!response.ok) {
            throw new Error(`HTTP Error! Status: ${response.status}`)
        }

        const games = await response.json();
        return games;
    } catch (error) {
        console.error('Error fetching game data: ', error);
        return [];
    }
}

function renderGameCard(game) {
    // Select the container where the game cards will be displayed
    const gameContainer = document.querySelector('.game-section');

    // Create the main game card container
    const gameCard = document.createElement('div');
    gameCard.classList.add('game-card');

    // Create hover animation wrapper
    const hoverAnimation = document.createElement('div');
    hoverAnimation.classList.add('hover-animation');

    // Add the card image
    const cardImage = document.createElement('div');
    cardImage.classList.add('card-image');
    const img = document.createElement('img');
    img.src = game.game_image;
    img.alt = game.title;
    cardImage.appendChild(img);
    hoverAnimation.appendChild(cardImage);

    // Add the card content
    const cardContent = document.createElement('div');
    cardContent.classList.add('card-content');

    const title = document.createElement('h2');
    title.classList.add('game-title');
    title.textContent = game.title;

    if (game.title.length > 31) {
        title.classList.add('long-title');
    }

    // Add the price and rating section
    const priceRatingSection = document.createElement('div');
    priceRatingSection.classList.add('price-rating-section');

    const priceSection = document.createElement('div');
    priceSection.classList.add('price-section');
    const price = document.createElement('span');
    price.classList.add('new-price');
    price.textContent = `$${game.price}`;
    priceSection.appendChild(price);

    const ratingSection = document.createElement('div');
    ratingSection.classList.add('rating-section');
    const ratingImg = document.createElement('img');
    ratingImg.src = "/static/assets/images/star-svgrepo-com.svg";
    ratingImg.alt = "";
    ratingImg.style.cssText = "height: 20px; width: 20px; margin-bottom: 0.2rem; margin-right: 0.2rem;";
    const ratingStars = document.createElement('span');
    ratingStars.classList.add('rating-stars');
    ratingStars.textContent = game.rating;
    const reviews = document.createElement('span');
    reviews.classList.add('reviews');
    reviews.textContent = `• ${game.reviews} reviews`;

    ratingSection.appendChild(ratingImg);
    ratingSection.appendChild(ratingStars);
    ratingSection.appendChild(reviews);

    priceRatingSection.appendChild(priceSection);
    priceRatingSection.appendChild(ratingSection);

    // Add description
    const description = document.createElement('p');
    description.classList.add('game-card-description');
    description.textContent = game.welcome_message;

    // Add "Read More" link
    const readMore = document.createElement('a');
    readMore.href = `game/${game.slug}/`;
    readMore.classList.add('read-more');
    readMore.textContent = 'Game Details';

    // Add buttons
    const cardButtons = document.createElement('div');
    cardButtons.classList.add('card-buttons');
    const addToCartButton = document.createElement('button');
    addToCartButton.classList.add('add-to-cart');
    addToCartButton.textContent = 'Add To Cart';
    // addToCartButton.setAttribute('data-game-id', game.id);
    addToCartButton.addEventListener('click', () => {
        addToCart(game.id);
    });

    const submitReviewButton = document.createElement('button');
    submitReviewButton.classList.add('submit-review');
    submitReviewButton.textContent = 'Submit A Review';

    const reviewPopup = document.getElementById("review-popup");
    const overlay = document.getElementById("overlay");

    submitReviewButton.addEventListener("click", () => {
        reviewPopup.style.display = "block";
        overlay.style.display = "block";
        document.body.style.overflow = "hidden";

        const reviewForm = document.getElementById('review-form');
        reviewForm.setAttribute('data-game-id', game.id);
    });

    cardButtons.appendChild(addToCartButton);
    cardButtons.appendChild(submitReviewButton);

    // Append everything to the card content
    cardContent.appendChild(title);
    cardContent.appendChild(priceRatingSection);
    cardContent.appendChild(description);
    cardContent.appendChild(readMore);
    cardContent.appendChild(cardButtons);

    // Append the content to the hover animation
    hoverAnimation.appendChild(cardContent);

    // Append the hover animation to the game card
    gameCard.appendChild(hoverAnimation);

    // Append the game card to the container
    gameContainer.appendChild(gameCard);
}

async function renderAllGames(franchise = null) {
    const gameContainer = document.querySelector('.game-section');

    while (gameContainer.firstChild) {
        gameContainer.removeChild(gameContainer.firstChild);
    }

    const games = await fetchGameData(franchise);

    games.forEach(game => renderGameCard(game));
}

document.querySelectorAll('.game-item').forEach(card => {
    card.addEventListener('click', (event) => {
        const franchise = event.currentTarget.getAttribute('data-franchise');

        const url = new URL(window.location);
        url.searchParams.set('franchise', franchise);
        window.history.pushState({}, '', url);

        renderAllGames(franchise);
    });
});

window.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const franchise = urlParams.get('franchise');

    renderAllGames(franchise);
})
