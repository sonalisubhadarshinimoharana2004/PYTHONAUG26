import React from 'react'
import { Link } from 'react-router'

function Navbar() {
  return (
    <div>
      <Link to="/">Home</Link> {" "}
      <Link to="/register">Register</Link>
    </div>
  )
}

export default Navbar
