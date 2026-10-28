import React, { useEffect, useState } from "react";
import axios from "axios";

import Register from "./components/Register";
import UserList from "./components/UserList";
import UpdateUser from "./components/UpdateUser";

const API_URL = "https://jsonplaceholder.typicode.com/users";

function App() {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // GET: Fetch users
  const fetchUsers = async () => {
    try {
      const response = await axios.get(API_URL);
      setUsers(response.data);
    } catch (error) {
      console.error("Error fetching users:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  // POST: Add user
  const handleUserAdded = (newUser) => {
    setUsers((previousUsers) => [
      ...previousUsers,
      {
        ...newUser,
        id: newUser.id ?? Date.now(),
      },
    ]);
  };

  // PUT: Update user in UI
  const handleUserUpdated = (updatedUser) => {
    setUsers((previousUsers) =>
      previousUsers.map((user) =>
        user.id === updatedUser.id ? updatedUser : user
      )
    );

    setSelectedUser(null);
  };

  // DELETE: Remove user
  const handleDelete = async (id) => {
    const confirmDelete = window.confirm(
      "Are you sure you want to delete this user?"
    );

    if (!confirmDelete) return;

    try {
      await axios.delete(`${API_URL}/${id}`);

      setUsers((previousUsers) =>
        previousUsers.filter((user) => user.id !== id)
      );

      if (selectedUser?.id === id) {
        setSelectedUser(null);
      }

      alert("User deleted successfully!");
    } catch (error) {
      console.error("Delete failed:", error);
      alert("Failed to delete user!");
    }
  };

  return (
    <div className="app">
      <h1>Axios CRUD Application</h1>

      <Register onUserAdded={handleUserAdded} />

      {selectedUser && (
        <UpdateUser
          selectedUser={selectedUser}
          onUserUpdated={handleUserUpdated}
          onCancel={() => setSelectedUser(null)}
        />
      )}

      {loading ? (
        <p className="loading">Loading users...</p>
      ) : (
        <UserList
          users={users}
          onEdit={setSelectedUser}
          onDelete={handleDelete}
        />
      )}
    </div>
  );
}

export default App;