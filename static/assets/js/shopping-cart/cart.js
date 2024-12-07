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
        const response = await fetch(`/shop/api/games/${slug}/`);

        if (!response.ok) {
            throw new Error('Failed to fetch game details');
        }

        const game = await response.json();

        return game.id;

    } catch (error) {
        console.error('Error fetching game details:', error);
    }
}

async function getCartId() {
    const response = await fetch('/api/cart/');
    const cartData = await response.json();

    return cartData.id;
}

async function checkout() {
    try {
        const response = await fetch('/interactions/api/checkout/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
        });

        if (!response.ok) {
            throw new Error('Failed to complete checkout');
        }

        // const orderData = await response.json();

        window.location.href = '/interactions/orders/';
    } catch (error) {
        console.error('Error during checkout: ', error);
    }
}

export {getCartId, checkout, getCSRFToken, getGameId, getGameSlugFromURL};