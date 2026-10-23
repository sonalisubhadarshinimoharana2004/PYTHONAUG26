import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-blue-600 text-white p-4 flex gap-6">
      <Link to="/" className="font-bold">
        Home
      </Link>

      <Link to="/details/101?name=Sonali&age=22&course=React">
        Details
      </Link>
    </nav>
  );
}

export default Navbar;
