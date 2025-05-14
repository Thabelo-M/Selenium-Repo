document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");
    const popup = document.getElementById("login-popup");
    const popupMessage = document.getElementById("login-popup-message");
    const closePopup = document.getElementById("close-popup");

    // Correct email and password
    const validEmail = "Selenium25@gmail.com";
    const validPassword = "Y0uMade1t&3&&";

    // Function to show popup message
    function showPopupMessage(message, isSuccess) {
        popupMessage.textContent = message;
        popup.style.display = "block";
        popupMessage.style.color = isSuccess ? "green" : "red";
    }

    // Close popup when button is clicked
    closePopup.addEventListener("click", function () {
        popup.style.display = "none";
    });

    // Handle login form submission
    loginForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const email = document.querySelector(".email").value.trim();
        const password = document.querySelector(".password").value.trim();

        // === New email domain validation ===
        if (!email.endsWith(".com") && !email.endsWith(".co.za")) {
            showPopupMessage("Email must end with .com or .co.za", false);
            return;
        }

        // === Credential check ===
        if (email === validEmail && password === validPassword) {
            showPopupMessage("You have successfully logged in!", true);

            // Redirect to Dashboard.html after successful login
            setTimeout(function() {
                window.location.href = "Dashboard.html"; // Redirect to Dashboard
            }, 1500); // Wait 1.5 seconds to let the user see the success message
        } else {
            showPopupMessage("Incorrect details!", false);
        }
    });
});