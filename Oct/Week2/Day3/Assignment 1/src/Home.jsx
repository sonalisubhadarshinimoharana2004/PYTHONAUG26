
import { useContext } from "react";
import { ThemeContext } from "../context/ThemeContext";

function Home() {
  const { theme } = useContext(ThemeContext);

  return (
    <main
      className={`min-h-[70vh] p-10 text-center ${
        theme === "dark"
          ? "bg-gray-800 text-white"
          : "bg-white text-gray-900"
      }`}
    >
      <h2 className="text-3xl font-bold mb-4">
        Welcome to My Website
      </h2>

      <p className="text-lg">
        This is a React Theme Switcher project.
      </p>

      <p className="mt-3">
        Current Theme: {theme.toUpperCase()}
      </p>
    </main>
  );
}

export default Home;