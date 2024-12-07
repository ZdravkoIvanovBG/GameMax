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
    const gameContainer = document.querySelector(".game-section");

    const card = document.createElement("div");
    card.classList.add("game-card");
    card.onclick = () => {
        window.location.href = `game/${game.slug}/`;
    };

    const cardImage = document.createElement("div");
    cardImage.classList.add("game-card-image");
    const img = document.createElement("img");
    img.src = game.game_image;
    img.alt = `Image of ${game.title}`;
    cardImage.appendChild(img);

    // Create the content section
    const cardContent = document.createElement("div");
    cardContent.classList.add("game-card-content");

    // Game title
    const title = document.createElement("h3");
    title.classList.add("game-title");
    title.textContent = game.title;

    // Game info (price, rating, reviews)
    const info = document.createElement("div");
    info.classList.add("game-info");

    const price = document.createElement("span");
    price.classList.add("game-price");
    price.textContent = `$${game.price}`; // Format price to two decimals

    const ratingPanel = document.createElement('span');
    ratingPanel.classList.add('game-rating');

    const starIcon = document.createElement('img');
    starIcon.src = '/static/assets/images/star-rating.png';
    starIcon.alt = "";
    starIcon.classList.add('star-icon');

    let tempRating = 0;

    if (game.reviews.length > 0) {
        for (let i = 0; i < game.reviews.length; i++) {
            tempRating += game.reviews[i].rating;
        }

        tempRating = (tempRating / game.reviews.length).toFixed(2);
    }

    const rating = document.createElement("span");
    rating.classList.add("game-rating");
    rating.textContent = tempRating;

    ratingPanel.appendChild(starIcon);
    ratingPanel.appendChild(rating);

    const reviews = document.createElement("span");
    reviews.classList.add("game-reviews");
    reviews.textContent = `${game.reviews.length} reviews`;

    // Append price, rating, and reviews to the info section
    info.appendChild(price);
    info.appendChild(ratingPanel);
    info.appendChild(reviews);

    // Append title and info to the card content
    cardContent.appendChild(title);
    cardContent.appendChild(info);

    // Append image and content to the main card
    card.appendChild(cardImage);
    card.appendChild(cardContent);

    // Append the card to the container
    gameContainer.appendChild(card);
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
