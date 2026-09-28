// ================================
// SELECT ELEMENTS
// ================================

let registerForm = document.getElementById("registerForm");
let loginForm = document.getElementById("loginForm");


// ================================
// REGISTER
// ================================

registerForm.addEventListener("submit", function (e) {

    e.preventDefault();

    // Get values
    let name = document.getElementById("name").value.trim();
    let age = document.getElementById("age").value.trim();
    let phone = document.getElementById("phone").value.trim();
    let email = document.getElementById("registerEmail").value.trim();
    let password = document.getElementById("registerPassword").value;

    let message = document.getElementById("registerMessage");


    // Clear previous message
    message.textContent = "";
    message.className = "message";


    // ================================
    // VALIDATION
    // ================================

    if (!name || !age || !phone || !email || !password) {

        message.textContent = "Please fill all fields.";
        message.classList.add("error");

        return;
    }


    // Age validation

    if (age < 1 || age > 120) {

        message.textContent = "Please enter a valid age.";
        message.classList.add("error");

        return;
    }


    // Phone validation

    if (!/^[0-9]{10}$/.test(phone)) {

        message.textContent =
            "Phone number must contain exactly 10 digits.";

        message.classList.add("error");

        return;
    }


    // Password validation

    if (password.length < 6) {

        message.textContent =
            "Password must contain at least 6 characters.";

        message.classList.add("error");

        return;
    }


    // ================================
    // GET EXISTING USERS
    // ================================

    let existingUsers =
        JSON.parse(localStorage.getItem("usersData")) || [];


    // ================================
    // CHECK EMAIL
    // ================================

    let userAlreadyExists =
        existingUsers.some(function (user) {

            return user.email.toLowerCase() === email.toLowerCase();

        });


    if (userAlreadyExists) {

        message.textContent =
            "An account with this email already exists.";

        message.classList.add("error");

        return;
    }


    // ================================
    // CREATE NEW USER
    // ================================

    let newUser = {

        name: name,

        age: age,

        phone: phone,

        email: email,

        password: password

    };


    // Add new user

    existingUsers.push(newUser);


    // Save to Local Storage

    localStorage.setItem(
        "usersData",
        JSON.stringify(existingUsers)
    );


    // ================================
    // SUCCESS
    // ================================

    message.textContent =
        "Registration successful! You can now login.";

    message.classList.add("success");


    // Clear form

    registerForm.reset();

});


// ================================
// LOGIN
// ================================

loginForm.addEventListener("submit", function (e) {

    e.preventDefault();


    let email =
        document.getElementById("loginEmail").value.trim();

    let password =
        document.getElementById("loginPassword").value;


    let message =
        document.getElementById("loginMessage");


    message.textContent = "";
    message.className = "message";


    // ================================
    // VALIDATION
    // ================================

    if (!email || !password) {

        message.textContent =
            "Please enter email and password.";

        message.classList.add("error");

        return;
    }


    // ================================
    // GET USERS
    // ================================

    let existingUsers =
        JSON.parse(localStorage.getItem("usersData")) || [];


    // ================================
    // FIND USER
    // ================================

    let existingUser = existingUsers.find(function (user) {

        return user.email.toLowerCase() === email.toLowerCase();

    });


    // ================================
    // USER NOT FOUND
    // ================================

    if (!existingUser) {

        message.textContent =
            "User does not exist. Please register first.";

        message.classList.add("error");

        return;
    }


    // ================================
    // CHECK PASSWORD
    // ================================

    if (existingUser.password !== password) {

        message.textContent =
            "Invalid password.";

        message.classList.add("error");

        return;
    }


    // ================================
    // LOGIN SUCCESS
    // ================================

    message.textContent =
        "Login successful! Welcome " + existingUser.name + " 🎉";

    message.classList.add("success");


    // Clear login form

    loginForm.reset();

});


// ================================
// SHOW LOGIN
// ================================

function showLogin() {

    document.querySelector(".register-box")
        .classList.add("hidden");

    document.querySelector(".login-box")
        .classList.remove("hidden");
}


// ================================
// SHOW REGISTER
// ================================

function showRegister() {

    document.querySelector(".login-box")
        .classList.add("hidden");

    document.querySelector(".register-box")
        .classList.remove("hidden");
}


// ================================
// SHOW / HIDE PASSWORD
// ================================

function togglePassword(inputId, button) {

    let input = document.getElementById(inputId);

    if (input.type === "password") {

        input.type = "text";

        button.textContent = "Hide";

    } else {

        input.type = "password";

        button.textContent = "Show";
    }
}