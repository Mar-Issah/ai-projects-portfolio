import { ArrowUpRight } from "lucide-react"
import { Link } from "react-router-dom"
import { motion } from "framer-motion"

import { Button } from "./ui/button"

export function ProjectCard({ project }) {
  return (
    <motion.article
      whileHover={{ y: -6 }}
      transition={{ duration: 0.2, ease: "easeOut" }}
      className="group h-full rounded-3xl border border-border/70 bg-card/90 p-6 shadow-sm"
    >
      <div className="flex items-center justify-between">
        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-muted-foreground">{project.id}</p>
        <div className="flex gap-2">
          {project.badges?.map((badge) => (
            <span key={badge} className="rounded-full bg-secondary px-3 py-1 text-xs font-medium text-secondary-foreground">
              {badge}
            </span>
          ))}
        </div>
      </div>

      <h3 className="mt-4 text-2xl font-semibold">{project.title}</h3>
      <p className="mt-2 text-sm text-muted-foreground">{project.description}</p>

      <div className="mt-6 flex items-center justify-between">
        <p className="text-sm font-medium text-muted-foreground">{project.tagline}</p>
        <Button asChild className="rounded-2xl">
          <Link to={project.path} className="flex items-center gap-1">
            Explore
            <ArrowUpRight className="h-4 w-4" />
          </Link>
        </Button>
      </div>
    </motion.article>
  )
}

