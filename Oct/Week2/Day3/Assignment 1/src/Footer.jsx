
import { useContext } from "react";
import { ThemeContext } from "../context/ThemeContext";

function Footer() {
  const { theme } = useContext(ThemeContext);

  return (
    <footer
      className={`p-5 text-center ${
        theme === "dark"
          ? "bg-black text-white"
          : "bg-blue-100 text-gray-900"
      }`}
    >
      <p>© 2026 My Website. All rights reserved.</p>
      <p className="mt-2">Built with React useContext.</p>
    </footer>
  );
}

export default Footer;