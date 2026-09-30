let registerForm = document.getElementById("registerForm");

registerForm.addEventListener("submit", function (e) {

    e.preventDefault();

    let name = document.getElementById("name").value.trim();
    let age = document.getElementById("age").value.trim();
    let phone = document.getElementById("phone").value.trim();
    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value;

    let message = document.getElementById("message");

    // Validation

    if (!name || !age || !phone || !email || !password) {

        message.textContent = "Please fill all the fields.";

        return;
    }

    if (phone.length !== 10) {

        message.textContent =
            "Phone number must contain 10 digits.";

        return;
    }

    if (password.length < 6) {

        message.textContent =
            "Password must contain at least 6 characters.";

        return;
    }

    // Create user object

    let user = {
        name: name,
        age: age,
        phone: phone,
        email: email,
        password: password
    };

    // Store data

    localStorage.setItem(
        "registeredUser",
        JSON.stringify(user)
    );

    message.textContent =
        "Registration successful!";

    // Clear form

    registerForm.reset();

});