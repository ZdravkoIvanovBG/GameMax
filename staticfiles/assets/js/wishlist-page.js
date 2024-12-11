import {getCSRFToken} from "./shopping-cart/cart.js";

const wishlistContainer = document.querySelector('.wishlist-container');

wishlistContainer.addEventListener('click', async function (event) {
    if (event.target && event.target.classList.contains('wishlist-remove-btn')) {
        const wishlistItemId = event.target.getAttribute('data-id');

        console.log(wishlistItemId);

        try {
            const response = await fetch(`/wishlist/api/delete/${wishlistItemId}/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
            });

            if (!response.ok) {
                throw new Error('Failed to remove item from wishlist.');
            }

            const itemElement = document.querySelector(`.wishlist-item[data-id="${wishlistItemId}"]`);
            if (itemElement) {
                itemElement.remove();
            }

            location.reload();

        } catch (error) {
            console.error('Error removing item from wishlist:', error);
        }
    }
});
