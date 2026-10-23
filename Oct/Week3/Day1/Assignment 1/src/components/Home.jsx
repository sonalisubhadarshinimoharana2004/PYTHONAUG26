import React from "react";
import { useNavigate } from "react-router";

function Home() {
  const navigate = useNavigate();

  function goToUser() {
    navigate("/user/101?name=Sonali&age=21&city=Cuttack");
  }

  return (
    <div>
      <h1>Home Page</h1>
      <p>Welcome to Home Page!</p>

      <button onClick={goToUser}>
        Go to User Page
      </button>
    </div>
  );
}

export default Home;
