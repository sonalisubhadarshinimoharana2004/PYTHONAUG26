let students = JSON.parse(localStorage.getItem("students")) || [];

let editId = null;

const form = document.getElementById("studentForm");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const courseInput = document.getElementById("course");
const table = document.getElementById("studentTable");
const submitBtn = document.getElementById("submitBtn");


// CREATE
form.addEventListener("submit", function (e) {

    e.preventDefault();

    const name = nameInput.value;
    const email = emailInput.value;
    const course = courseInput.value;

    if (editId === null) {

        const student = {
            id: Date.now(),
            name: name,
            email: email,
            course: course
        };

        students.push(student);

    } else {

        // UPDATE
        students = students.map(function (student) {

            if (student.id === editId) {
                return {
                    id: student.id,
                    name: name,
                    email: email,
                    course: course
                };
            }

            return student;
        });

        editId = null;
        submitBtn.textContent = "Add Student";
    }

    localStorage.setItem("students", JSON.stringify(students));

    form.reset();

    displayStudents();
});


// READ
function displayStudents() {

    table.innerHTML = "";

    students.forEach(function (student) {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.email}</td>
            <td>${student.course}</td>

            <td>
                <button onclick="editStudent(${student.id})">
                    Edit
                </button>

                <button onclick="deleteStudent(${student.id})">
                    Delete
                </button>
            </td>
        `;

        table.appendChild(row);
    });
}


// UPDATE
function editStudent(id) {

    const student = students.find(function (student) {
        return student.id === id;
    });

    nameInput.value = student.name;
    emailInput.value = student.email;
    courseInput.value = student.course;

    editId = id;

    submitBtn.textContent = "Update Student";
}


// DELETE
function deleteStudent(id) {

    const confirmDelete = confirm("Are you sure you want to delete this student?");

    if (confirmDelete) {

        students = students.filter(function (student) {
            return student.id !== id;
        });

        localStorage.setItem("students", JSON.stringify(students));

        displayStudents();
    }
}


// Display data when page loads
displayStudents();