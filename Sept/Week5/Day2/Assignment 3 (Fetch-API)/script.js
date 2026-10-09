let fetchBtn = document.getElementById("fetchBtn");

let postsDiv = document.getElementById("posts");


fetchBtn.addEventListener("click", function () {

    postsDiv.innerHTML = "Loading...";


    fetch("https://jsonplaceholder.typicode.com/posts")

        .then(function (response) {

            return response.json();

        })

        .then(function (data) {

            postsDiv.innerHTML = "";


            data.forEach(function (post) {

                let postDiv =
                    document.createElement("div");


                postDiv.innerHTML = `
                    <h2>${post.id}. ${post.title}</h2>
                    <p>${post.body}</p>
                    <hr>
                `;


                postsDiv.appendChild(postDiv);

            });

        })

        .catch(function (error) {

            postsDiv.innerHTML =
                "Error fetching data.";

            console.log(error);

        });

});