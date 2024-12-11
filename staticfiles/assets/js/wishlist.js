import {getGameSlugFromURL, getCSRFToken, getGameId} from "./shopping-cart/cart.js";

const addToWishlistButton = document.getElementById('add-to-wishlist');

addToWishlistButton.addEventListener('click', async function () {
    const gameSlug = getGameSlugFromURL()

    const gameId = await getGameId(gameSlug);

    try {
        const response = await fetch('/wishlist/api/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
            body: JSON.stringify({
                game: gameId
            }),
        });

        const data = await response.json()

        if (data.message === "In Cart") {
            showCustomAlert('The game is already in the wishlist!', 'error');
            return;
        }

        if (response.status === 403) {
            window.location.href = '/accounts/login/';
            return;
        }

        if (!response.ok) {
            throw new Error('Failed to add game to wishlist');
        }

        showCustomAlert('Your game has been successfully added to your wishlist!', 'success');

    } catch (error) {
        console.error('Error adding to wishlist:', error);
        showCustomAlert('Something went wrong! Please try again.', 'error');
    }
})

function showCustomAlert(message, type) {
    const customAlertMessage = document.getElementById('customAlertMessage');
    const alertMessageContent = document.getElementById('alertMessageContent');

    customAlertMessage.style.display = 'flex';
    document.getElementById('alertMessageText').textContent = message;
    alertMessageContent.classList.add(type);
    document.getElementById('alertMessageHeader').textContent = type === 'success' ? 'Success!' : 'Error!';

    alertMessageContent.style.animation = 'none';
    alertMessageContent.offsetHeight;
    alertMessageContent.style.animation = 'fadeIn 1s forwards';

    setTimeout(function () {
        document.getElementById("alertMessageContent").style.animation = "fadeOut 1s forwards";
    }, 1500);

    document.getElementById("closeAlertMessage").onclick = function () {
        document.getElementById("customAlertMessage").style.display = "none";
    };
}
