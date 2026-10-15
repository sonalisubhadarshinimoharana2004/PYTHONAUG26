
import { useContext } from "react";
import { ThemeContext } from "../context/ThemeContext";

function Navbar() {
  const { theme, toggleLight, toggleDark } =
    useContext(ThemeContext);

  return (
    <nav
      className={`p-5 flex flex-wrap justify-between items-center gap-4 ${
        theme === "dark"
          ? "bg-gray-900 text-white"
          : "bg-blue-100 text-gray-900"
      }`}
    >
      <h1 className="text-2xl font-bold">My Website</h1>

      <div className="flex gap-3">
        <button
          onClick={toggleLight}
          className="bg-yellow-400 text-black px-4 py-2 rounded"
        >
          Light Mode
        </button>

        <button
          onClick={toggleDark}
          className="bg-gray-700 text-white px-4 py-2 rounded"
        >
          Dark Mode
        </button>
      </div>
    </nav>
  );
}

export default Navbar;