import React from "react";
import { Link } from "react-router";

function Navbar() {
  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
      <Link to="/user/101?name=Sonali&age=21&city=Cuttack">
        User
      </Link>
    </nav>
  );
}

export default Navbar;
