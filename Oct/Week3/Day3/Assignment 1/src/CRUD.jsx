import React, { useEffect, useState } from "react";
import axios from "axios";
function CRUD() {
  const API = "https://jsonplaceholder.typicode.com/users";

  const [users, setUsers] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [editId, setEditId] = useState(null);
  const [loading, setLoading] = useState(false);

  // READ: Get all users
  const getUsers = async () => {
    try {
      setLoading(true);

      const res = await axios.get(API);

      setUsers(res.data);
    } catch (error) {
      console.log("Error fetching users:", error);
      alert("Unable to fetch users");
    } finally {
      setLoading(false);
    }
  };

  // CREATE and UPDATE
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!name.trim() || !email.trim()) {
      alert("Please enter name and email");
      return;
    }

    try {
      if (editId === null) {
        // CREATE: Add new user
        const res = await axios.post(API, {
          name: name,
          email: email,
        });

        // Add the created user to the UI
        setUsers((prevUsers) => [
          ...prevUsers,
          {
            ...res.data,
            id: Date.now(),
            name: res.data.name,
            email: res.data.email,
          },
        ]);

        alert("User created successfully!");
      } else {
        // UPDATE: Update existing user
        const res = await axios.put(`${API}/${editId}`, {
          name: name,
          email: email,
        });

        setUsers((prevUsers) =>
          prevUsers.map((user) =>
            user.id === editId
              ? { ...user, ...res.data, id: editId }
              : user
          )
        );

        alert("User updated successfully!");
      }

      setName("");
      setEmail("");
      setEditId(null);
    } catch (error) {
      console.log("Error submitting user:", error);
      alert("Operation failed");
    }
  };

  // Load user details into the form
  const handleEdit = (user) => {
    setName(user.name);
    setEmail(user.email);
    setEditId(user.id);
  };

  // DELETE: Remove user
  const handleDelete = async (id) => {
    const confirmDelete = window.confirm(
      "Are you sure you want to delete this user?"
    );

    if (!confirmDelete) return;

    try {
      await axios.delete(`${API}/${id}`);

      setUsers((prevUsers) =>
        prevUsers.filter((user) => user.id !== id)
      );

      if (editId === id) {
        setName("");
        setEmail("");
        setEditId(null);
      }

      alert("User deleted successfully!");
    } catch (error) {
      console.log("Error deleting user:", error);
      alert("Unable to delete user");
    }
  };

  // GET API call on first render
  useEffect(() => {
    getUsers();
  }, []);

  return (
    <div style={styles.container}>
      <h1>Axios CRUD Operations</h1>

      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          type="text"
          placeholder="Enter your name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <button type="submit">
          {editId === null ? "Create User" : "Update User"}
        </button>

        {editId !== null && (
          <button
            type="button"
            onClick={() => {
              setEditId(null);
              setName("");
              setEmail("");
            }}
          >
            Cancel
          </button>
        )}
      </form>

      <h2>User List</h2>

      {loading ? (
        <p>Loading users...</p>
      ) : users.length === 0 ? (
        <p>No users found.</p>
      ) : (
        <table style={styles.table}>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>
            {users.map((user) => (
              <tr key={user.id}>
                <td>{user.id}</td>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>
                  <button onClick={() => handleEdit(user)}>
                    Edit
                  </button>

                  <button
                    onClick={() => handleDelete(user.id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "900px",
    margin: "30px auto",
    padding: "20px",
    fontFamily: "Arial, sans-serif",
  },

  form: {
    display: "flex",
    flexWrap: "wrap",
    gap: "10px",
    marginBottom: "25px",
  },

  table: {
    width: "100%",
    borderCollapse: "collapse",
    textAlign: "left",
  },
};

export default CRUD;

