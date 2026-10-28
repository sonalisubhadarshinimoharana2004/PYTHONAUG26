import React, { useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";

function Register() {
  let [formData, setFormData] = useState({
    fullName: "",
    phone: "",
    email: "",
    password: "",
  });

  function handleInput(e) {
    let { name, value } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  }


  async function handleRegister(e){
    e.preventDefault();
    
    try {
        let result=await axios.post("https://jsonplaceholder.typicode.com/users",formData);

        console.log(result.data);

        toast.success("register successfully")
    } catch (error) {
        console.log("error",error)
    }
  }

  return (
    <div>
      <form onSubmit={handleRegister}>
        <label htmlFor="">Full Name</label>
        <input
          type="text"
          placeholder="Enter your name"
          name="fullName"
          value={formData.fullName}
          onChange={handleInput}
        />
        <br />
        <label htmlFor="">Phone</label>
        <input
          type="number"
          placeholder="Enter your Phone number"
          name="phone"
          value={formData.phone}
          onChange={handleInput}
        />{" "}
        <br />
        <label htmlFor="">Email</label>
        <input
          type="email"
          placeholder="Enter your email"
          name="email"
          value={formData.email}
          onChange={handleInput}
        />
        <br />
        <label htmlFor="">Password</label>
        <input
          type="password"
          placeholder="Enter your password"
          name="password"
          value={formData.password}
          onChange={handleInput}
        />
        <br />
        <button>Register</button>
      </form>
    </div>
  );
}

export default Register;
