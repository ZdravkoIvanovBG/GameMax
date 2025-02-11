import {getCartId, checkout, getGameId, getGameSlugFromURL, getCSRFToken} from "./cart.js";

async function fetchGameDetails(slug) {
    try {
        const response = await fetch(`/shop/api/games/${slug}`);

        if (!response.ok) {
            throw new Error('Failed to fetch game details.')
        }

        return await response.json();

    } catch (error) {
        console.error('Error fetching game details:', error);
        return null;
    }
}

async function fetchCartData() {
    try {
        let apiURL = '/api/cart/';

        const response = await fetch(apiURL);

        if (!response.ok) {
            throw new Error('Failed to fetch cart');
        }

        const cartData = await response.json();

        renderCart(cartData.items);
        updateCartCount(cartData.items);
        updateTotalPrice(cartData.total_price);
    } catch (error) {
        console.error('Error fetching cart data:', error);
    }
}

function updateCartCount(cartItems) {
    const cartCount = document.getElementById("cart-count");
    cartCount.textContent = cartItems.length; // Update the badge with the number of items in the cart
}

function updateTotalPrice(totalPrice) {
    document.getElementById('cart-total').textContent = `$${totalPrice}`
}

async function renderCart(cartItems) {
    const cartItemsContainer = document.querySelector(".cart-items");

    while (cartItemsContainer.firstChild) {
        cartItemsContainer.removeChild(cartItemsContainer.firstChild);
    }

    if (cartItems.length === 0) {
        const emptyMessage = document.createElement("p");
        emptyMessage.classList.add("empty-cart-message");
        emptyMessage.textContent = "Your cart is empty.";
        cartItemsContainer.appendChild(emptyMessage);
        return;
    }

    for (const item of cartItems) {
        const game = await fetchGameDetails(item['game'].slug);

        const cartItem = document.createElement("div");
        cartItem.classList.add("cart-item");

        const itemImage = document.createElement("img");
        itemImage.src = game.game_image;
        itemImage.alt = `${game.title} Thumbnail`;
        itemImage.classList.add("cart-item-image");

        const itemDetails = document.createElement("div");
        itemDetails.classList.add("cart-item-details");

        const itemTitle = document.createElement("h4");
        itemTitle.classList.add("cart-item-title");
        itemTitle.textContent = game.title;

        const removeLink = document.createElement("a");
        removeLink.href = "#";
        removeLink.classList.add("cart-item-remove");
        removeLink.textContent = "Remove";
        removeLink.addEventListener("click", () => removeFromCart(item.id));

        itemDetails.appendChild(itemTitle);
        itemDetails.appendChild(removeLink);

        const itemGenre = document.createElement("div");
        itemGenre.classList.add("cart-item-genre");
        itemGenre.textContent = game.genre;

        const itemPrice = document.createElement("div");
        itemPrice.classList.add("cart-item-price");
        itemPrice.textContent = `$${game.price}`

        cartItem.appendChild(itemImage);
        cartItem.appendChild(itemDetails);
        cartItem.appendChild(itemGenre);
        cartItem.appendChild(itemPrice);

        cartItemsContainer.appendChild(cartItem);
    }

    updateCartCount(cartItems);
}

async function addToCart(gameId) {
    const cartId = await getCartId();

    if (!cartId) {
        console.error('Cart ID not found');
        return;
    }

    const csrfToken = getCSRFToken();

    if (!csrfToken) {
        console.error('CSRF token not found');
        return;
    }

    try {
        const response = await fetch('/shop/api/cart/add/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({
                cart: cartId,
                game: gameId
            }),
        });

        if (response.status === 401) {
            window.location.href = '/accounts/login/';
            return;
        }

        if (!response.ok) {
            throw new Error('Failed to add to cart');
        }

        await fetchCartData();

    } catch (error) {
        console.error('Error adding to cart: ', error);
    }
}

async function removeFromCart(cartItemId) {
    const csrfToken = getCSRFToken();

    if (!csrfToken) {
        console.error('CSRF token not found');
        return;
    }

    try {
        const response = await fetch(`/shop/api/cart/remove/${cartItemId}/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
        });

        if (response.status === 403) {
            window.location.href = '/accounts/login/';
            return;
        }

        if (!response.ok) {
            throw new Error('Failed to remove item from cart');
        }

        await fetchCartData();
    } catch (error) {
        console.error('Error removing item from cart: ', error);
    }

}

document.addEventListener('DOMContentLoaded', () => {
    fetchCartData();

    const addToCartButton = document.getElementById('add-to-cart');

    if (addToCartButton) {
        addToCartButton.addEventListener('click', async () => {
            const slug = getGameSlugFromURL();

            if (!slug) {
                console.error('Game slug not found!');
                return;
            }

            const gameId = await getGameId(slug);

            if (gameId) {
                addToCart(gameId);
            } else {
                console.error('Game ID not found!');
            }
        })
    }

    const checkoutButton = document.getElementById('checkout');

    if (checkoutButton) {
        checkoutButton.addEventListener('click', () => {
            checkout();
        })
    }
});
