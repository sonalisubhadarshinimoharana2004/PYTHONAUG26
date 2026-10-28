import React, { useEffect, useState } from "react";
import axios from "axios";

function UpdateUser({ selectedUser, onUserUpdated, onCancel }) {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    username: "",
  });

  useEffect(() => {
    if (selectedUser) {
      setFormData({
        name: selectedUser.name || "",
        email: selectedUser.email || "",
        username: selectedUser.username || "",
      });
    }
  }, [selectedUser]);

  if (!selectedUser) {
    return null;
  }

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleUpdate = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.put(
        `https://jsonplaceholder.typicode.com/users/${selectedUser.id}`,
        {
          ...selectedUser,
          ...formData,
        }
      );

      onUserUpdated({
        ...selectedUser,
        ...response.data,
        ...formData,
      });

      alert("User updated successfully!");
    } catch (error) {
      console.error("Update failed:", error);
      alert("Failed to update user!");
    }
  };

  return (
    <div className="form-container">
      <h2>Update User</h2>

      <form onSubmit={handleUpdate}>
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

        <button type="submit">Update</button>

        <button type="button" onClick={onCancel}>
          Cancel
        </button>
      </form>
    </div>
  );
}

export default UpdateUser;