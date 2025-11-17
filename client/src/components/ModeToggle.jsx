import { Moon, Sun } from "lucide-react"
import { useEffect, useState } from "react"

import { Button } from "./ui/button"

const themes = {
  light: "light",
  dark: "dark",
}

export function ModeToggle() {
  const [theme, setTheme] = useState(() => {
    if (typeof window === "undefined") return themes.light
    return localStorage.getItem("theme") || themes.light
  })

  useEffect(() => {
    const root = document.documentElement
    root.classList.remove(theme === themes.light ? themes.dark : themes.light)
    root.classList.add(theme)
    localStorage.setItem("theme", theme)
  }, [theme])

  const handleToggle = () => {
    setTheme((prev) => (prev === themes.light ? themes.dark : themes.light))
  }

  return (
    <Button
      variant="outline"
      size="icon"
      className="rounded-2xl"
      onClick={handleToggle}
      aria-label="Toggle dark mode"
    >
      {theme === themes.light ? <Moon className="h-5 w-5" /> : <Sun className="h-5 w-5" />}
    </Button>
  )
}

