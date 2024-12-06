const allStar = document.querySelectorAll(".rating .star");
const ratingValue = document.querySelector(".rating input");

allStar.forEach((item, idx) => {
    item.addEventListener("click", function () {
        let click = 0;
        ratingValue.value = idx + 1;

        allStar.forEach((i) => {
            i.classList.replace("bxs-star", "bx-star");
            i.classList.remove("active");
        });
        for (let i = 0; i < allStar.length; i++) {
            if (i <= idx) {
                allStar[i].classList.replace("bx-star", "bxs-star");
                allStar[i].classList.add("active");
            } else {
                allStar[i].style.setProperty("--i", click);
                click++;
            }
        }
    });
});

const reviewPopup = document.getElementById("review-popup");
const overlay = document.getElementById("overlay");
const cancelBtn = document.getElementById("cancel-btn");
const stars = document.querySelectorAll(".star");
const ratingInput = document.querySelector('[name="rating"]');

cancelBtn.addEventListener("click", closePopup);

function closePopup() {
    reviewPopup.style.display = "none";
    overlay.style.display = "none";
    document.body.style.overflow = "auto";
}

const reviewForm = document.getElementById('review-form');
const reviewInput = reviewForm.querySelector('textarea[name="opinion"]');

async function ReviewSubmission(gameId) {
    const rating = ratingInput.value;
    const review_text = reviewInput.value;

    if (!rating) {
        alert("Please provide a rating");
        return;
    }

    try {
        const response = await fetch('/interactions/api/reviews/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
            body: JSON.stringify({
                rating: rating,
                review_text: review_text,
                game: gameId
            }),
        });

        if (!response.ok) {
            throw new Error('Failed to submit review.');
        }

    } catch (error) {
        console.error('Error submitting review: ', error);
    }
}

document.querySelectorAll('.submit').forEach((button) => {
    button.addEventListener('click', () => {
        const gameId = button.getAttribute('data-game-id');

        ReviewSubmission(gameId);
    });
});
