import { Sparkles } from 'lucide-react';
import { Link } from 'react-router-dom';

import { ProjectCard } from '../components/ProjectCard';
import { Button } from '../components/ui/button';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/ui/tabs';
import { projects } from '../data/projects';

export default function HomePage() {
  return (
    <main className='mx-auto flex max-w-6xl flex-col gap-16 px-6 py-12'>
      <Hero />
      <Projects />
      <Footer />
    </main>
  );
}

function Hero() {
  return (
    <section>
      <p className='inline-flex items-center gap-2 rounded-full border border-border/80 px-4 py-1 text-xs font-semibold uppercase tracking-[0.2em] text-primary'>
        <Sparkles className='h-4 w-4' /> Machines are learning, so am I
      </p>
    </section>
  );
}

function Projects() {
  return (
    <section className='space-y-6'>
      <div>
        <p className='text-xs font-semibold uppercase tracking-[0.2em] text-primary'>Projects</p>
        <h2 className='mt-2 text-3xl font-semibold'>AI adventures</h2>
      </div>
      <div className='grid gap-6 md:grid-cols-2'>
        {projects.map((project) => (
          <ProjectCard key={project.id} project={project} />
        ))}
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className='flex flex-col gap-2 pb-8 text-sm text-muted-foreground md:flex-row md:items-center md:justify-between'>
      <p>© {new Date().getFullYear()} Marsiya. Built with React, Tailwind, shadcn/ui.</p>
      <p>
        Contact:{' '}
        <a href='mailto:masy370@gmail.com' className='text-primary underline'>
          masy370@gmail.com
        </a>
      </p>
    </footer>
  );
}
