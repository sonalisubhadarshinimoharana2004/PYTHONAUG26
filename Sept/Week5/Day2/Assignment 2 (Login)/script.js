let loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", function (e) {

    e.preventDefault();

    let email = document.getElementById("email").value.trim();

    let password =
        document.getElementById("password").value;

    let message =
        document.getElementById("message");


    // Validation

    if (!email || !password) {

        message.textContent =
            "Please enter email and password.";

        return;
    }


    // Get registered user

    let user = JSON.parse(
        localStorage.getItem("registeredUser")
    );


    // Check user

    if (!user) {

        message.textContent =
            "User not registered. Please register first.";

        return;
    }


    // Check email

    if (user.email !== email) {

        message.textContent =
            "Invalid email.";

        return;
    }


    // Check password

    if (user.password !== password) {

        message.textContent =
            "Invalid password.";

        return;
    }


    // Login successful

    message.textContent =
        "Login successful! Welcome " + user.name;

    loginForm.reset();

});