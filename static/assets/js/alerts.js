setTimeout(function () {
    // Add fade-out animation
    document.getElementById("alertMessageContent").style.animation =
        "fadeOut 1s forwards"; // Apply fade-out animation
}, 1500);

document.getElementById("closeAlertMessage").onclick = function () {
    document.getElementById("customAlertMessage").style.display = "none";
};
