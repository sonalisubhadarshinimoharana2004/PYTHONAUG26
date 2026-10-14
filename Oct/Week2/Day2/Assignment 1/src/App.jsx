import React, { useState } from "react";

function App() {
  const [formData, setFormData] = useState({
    name: "",
    age: "",
    email: "",
  });

  const [userData, setUserData] = useState(null);

  const handleInput = (e) => {
    const { name, value } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    localStorage.setItem("Datauser", JSON.stringify(formData));
    setUserData({ ...formData });

    setFormData({
      name: "",
      age: "",
      email: "",
    });
  };

  return (
    <div className="max-w-lg mx-auto mt-10 p-6">
      <h1 className="text-3xl font-bold text-center mb-6">
        Student Registration
      </h1>

      <form
        onSubmit={handleSubmit}
        className="border p-6 rounded-xl shadow-lg space-y-4"
      >
        <input
          type="text"
          name="name"
          placeholder="Enter your name"
          value={formData.name}
          onChange={handleInput}
          required
          className="w-full border p-2 rounded"
        />

        <input
          type="number"
          name="age"
          placeholder="Enter your age"
          value={formData.age}
          onChange={handleInput}
          min="1"
          required
          className="w-full border p-2 rounded"
        />

        <input
          type="email"
          name="email"
          placeholder="Enter your email"
          value={formData.email}
          onChange={handleInput}
          required
          className="w-full border p-2 rounded"
        />

        <button
          type="submit"
          className="w-full bg-purple-600 text-white p-2 rounded hover:bg-purple-700"
        >
          Register
        </button>
      </form>

      {userData && (
        <div className="mt-6 border p-5 rounded-xl shadow">
          <h2 className="text-xl font-bold text-green-600 mb-3">
            Registration Successful!
          </h2>

          <p><strong>Name:</strong> {userData.name}</p>
          <p><strong>Age:</strong> {userData.age}</p>
          <p><strong>Email:</strong> {userData.email}</p>
        </div>
      )}
    </div>
  );
}

export default App;