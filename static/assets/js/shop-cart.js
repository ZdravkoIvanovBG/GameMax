async function fetchCartData() {
    try {
        let apiURL = 'api/cart/';

        const response = await fetch(apiURL);

        if (!response.ok) {
            throw new Error('Failed to fetch cart');
        }

        const cartData = await response.json();

        await renderCart(cartData.items);
        updateTotalPrice(cartData.total_price);
    } catch (error) {
        console.error('Error fetching cart data:', error);
    }
}

async function fetchGameDetails(gameId) {
    try {
        const response = await fetch(`api/games/${gameId}`);

        if (!response.ok) {
            throw new Error('Failed to fetch game details.')
        }

        return await response.json();

    } catch (error) {
        console.error('Error fetching game details:', error);
        return null;
    }
}

async function getCartId() {
    const response = await fetch('api/cart/');
    const cartData = await response.json();

    // console.log(cartData.id);
    return cartData.id;
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

    // Check if cart is empty
    if (cartItems.length === 0) {
        const emptyMessage = document.createElement("p");
        emptyMessage.classList.add("empty-cart-message");
        emptyMessage.textContent = "Your cart is empty.";
        cartItemsContainer.appendChild(emptyMessage);
        return;
    }

    // Render each cart item
    for (const item of cartItems) {
        const game = await fetchGameDetails(item['game']);

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
        // Add event listener for removing items (not implemented yet)
        // removeLink.addEventListener("click", () => removeItemFromCart(item.id));

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

    // Update the cart count badge
    updateCartCount(cartItems);
}

document.addEventListener('DOMContentLoaded', fetchCartData);

function getCSRFToken() {
    const csrfToken = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));

    return csrfToken ? csrfToken.split('=')[1] : null;
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
        const response = await fetch('api/cart/add/', {
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

        if (!response.ok) {
            throw new Error('Failed to add to cart');
        }

        fetchCartData();

    } catch (error) {
        console.error('Error adding to cart: ', error);
    }
}
