import React, { useState } from "react";
import axios from "axios";

function Register({ onUserAdded }) {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    username: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        "https://jsonplaceholder.typicode.com/users",
        formData
      );

      onUserAdded(response.data);

      alert("User registered successfully!");

      setFormData({
        name: "",
        email: "",
        username: "",
      });
    } catch (error) {
      console.error("Registration failed:", error);
      alert("Registration failed!");
    }
  };

  return (
    <div className="form-container">
      <h2>Register User</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Enter Name"
          value={formData.name}
          onChange={handleChange}
          required
        />

        <input
          type="email"
          name="email"
          placeholder="Enter Email"
          value={formData.email}
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="username"
          placeholder="Enter Username"
          value={formData.username}
          onChange={handleChange}
          required
        />

        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default Register;