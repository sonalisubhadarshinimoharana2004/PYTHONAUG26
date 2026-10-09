const form = document.getElementById("studentForm");
const message = document.getElementById("message");
const details = document.getElementById("details");
const viewBtn = document.getElementById("viewBtn");


// Register Student
form.addEventListener("submit", function(event) {

    event.preventDefault();

    // Get values
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const dob = document.getElementById("dob").value;
    const address = document.getElementById("address").value.trim();

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

    if (phone === "") {
        message.textContent = "Please enter your phone number.";
        return;
    }

    if (dob === "") {
        message.textContent = "Please select your date of birth.";
        return;
    }

    if (!gender) {
        message.textContent = "Please select your gender.";
        return;
    }

    if (address === "") {
        message.textContent = "Please enter your address.";
        return;
    }


    // Create student object
    const student = {
        name: name,
        email: email,
        phone: phone,
        dob: dob,
        gender: gender.value,
        address: address
    };


    // Store in Local Storage
    localStorage.setItem(
        "studentData",
        JSON.stringify(student)
    );


    // Success message
    message.textContent = "Registration successful!";
    message.style.color = "green";


    // Clear form
    form.reset();

});


// View Details
viewBtn.addEventListener("click", function() {

    const savedData = localStorage.getItem("studentData");

    if (!savedData) {
        details.innerHTML = "<p>No student details found.</p>";
        return;
    }

    const student = JSON.parse(savedData);

    details.innerHTML = `
        <h2>Student Details</h2>

        <p><strong>Name:</strong> ${student.name}</p>

        <p><strong>Email:</strong> ${student.email}</p>

        <p><strong>Phone:</strong> ${student.phone}</p>

        <p><strong>Date of Birth:</strong> ${student.dob}</p>

        <p><strong>Gender:</strong> ${student.gender}</p>

        <p><strong>Address:</strong> ${student.address}</p>
    `;

});