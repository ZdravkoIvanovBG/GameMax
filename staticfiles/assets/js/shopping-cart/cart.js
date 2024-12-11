const API_URLS = {
    cart: '/api/cart/',
    gameDetails: slug => `/shop/api/games/${slug}/`,
    checkout: '/orders/api/checkout/',
}

function showError(message) {
    alert(message);
}

function getCSRFToken() {
    const csrfToken = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));

    return csrfToken ? csrfToken.split('=')[1] : null;
}

function getGameSlugFromURL() {
    const urlParts = window.location.pathname.split('/');

    return urlParts[urlParts.length - 2];
}

async function getGameId(slug) {
    try {
        const response = await fetch(API_URLS.gameDetails(slug));

        if (!response.ok) {
            throw new Error('Failed to fetch game details');
        }

        const game = await response.json();

        return game.id;

    } catch (error) {
        console.error('Error fetching game ID:', error);
        return null;
    }
}

async function getCartId() {
    const response = await fetch(API_URLS.cart);
    const cartData = await response.json();

    return cartData.id;
}

async function checkout() {
    try {
        const response = await fetch(API_URLS.checkout, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
        });

        if (!response.ok) {
            if (response.status === 400) {
                showCustomAlert('Please add games to the cart!', 'error');
                return;
            }
        }
        window.location.href = '/orders/';
    } catch
        (error) {
        showCustomAlert('Please add games to the cart!', 'error');
    }
}

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

export {getCartId, checkout, getCSRFToken, getGameId, getGameSlugFromURL};