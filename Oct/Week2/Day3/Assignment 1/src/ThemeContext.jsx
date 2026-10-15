
import { createContext, useState, useEffect } from "react";

export const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState(() => {
    return localStorage.getItem("theme") || "light";
  });

  useEffect(() => {
    localStorage.setItem("theme", theme);
  }, [theme]);

  const toggleLight = () => setTheme("light");
  const toggleDark = () => setTheme("dark");

  return (
    <ThemeContext.Provider
      value={{ theme, toggleLight, toggleDark }}
    >
      {children}
    </ThemeContext.Provider>
  );
}