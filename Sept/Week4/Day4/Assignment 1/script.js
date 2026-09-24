const form = document.getElementById("registrationForm");
const message = document.getElementById("message");

form.addEventListener("submit", function(event) {

    event.preventDefault();

    // Get form values
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const course = document.getElementById("course").value;
    const password = document.getElementById("password").value;
    const confirmPassword =
        document.getElementById("confirmPassword").value;

    const gender = document.querySelector(
        'input[name="gender"]:checked'
    );

    // Validation
    if (name === "") {
        message.textContent = "Please enter your name.";
        return;
    }

    if (email === "") {
        message.textContent = "Please enter your email.";
        return;
    }

    if (!/^[0-9]{10}$/.test(phone)) {
        message.textContent = "Enter a valid 10-digit phone number.";
        return;
    }

    if (!gender) {
        message.textContent = "Please select your gender.";
        return;
    }

    if (course === "") {
        message.textContent = "Please select a course.";
        return;
    }

    if (password.length < 6) {
        message.textContent =
            "Password must contain at least 6 characters.";
        return;
    }

    if (password !== confirmPassword) {
        message.textContent = "Passwords do not match.";
        return;
    }

    // Create student object
    const student = {
        name: name,
        email: email,
        phone: phone,
        gender: gender.value,
        course: course,
        password: password
    };

    // Get existing students
    let students =
        JSON.parse(localStorage.getItem("students")) || [];

    // Add new student
    students.push(student);

    // Save data
    localStorage.setItem(
        "students",
        JSON.stringify(students)
    );

    // Success message
    message.textContent = "Registration successful!";
    message.style.color = "green";

    // Clear form
    form.reset();
});