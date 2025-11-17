import { AnimatePresence } from 'framer-motion';
import { Link, useLocation } from 'react-router-dom';
import { Menu, X } from 'lucide-react';
import { useEffect, useState } from 'react';

import logo from '../assets/logo.svg';
import { projects } from '../data/projects';
import { ModeToggle } from './ModeToggle';
import { Button } from './ui/button';
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from './ui/dropdown-menu';

export function Navbar() {
  const [mobileOpen, setMobileOpen] = useState(false);
  const [projectsOpen, setProjectsOpen] = useState(false);
  const location = useLocation();

  useEffect(() => {
    setMobileOpen(false);
    setProjectsOpen(false);
  }, [location.pathname]);

  const renderProjectLinks = (onNavigate = () => setProjectsOpen(false)) =>
    projects.map((project) => (
      <DropdownMenuItem key={project.path} asChild className='flex-col items-start gap-1 rounded-2xl p-3'>
        <Link to={project.path} onClick={onNavigate} className='w-full'>
          <p className='text-sm font-semibold'>{project.title}</p>
          <p className='text-xs text-muted-foreground'>{project.tagline}</p>
        </Link>
      </DropdownMenuItem>
    ));

  return (
    <header className='sticky top-0 z-40 border-b border-border/60 bg-background/80 backdrop-blur-xl'>
      <div className='mx-auto flex max-w-6xl items-center justify-between px-6 py-4'>
        <Link to='/' className='flex items-center gap-3 text-lg font-semibold tracking-tight'>
          <img src={logo} alt='Marsiya Labs logo' className='h-10 w-10 rounded-2xl shadow-sm' />
          Marsiya Labs
        </Link>

        <nav className='hidden items-center gap-6 md:flex'>
          <DropdownMenu open={projectsOpen} onOpenChange={setProjectsOpen}>
            <DropdownMenuTrigger asChild>
              <Button variant='ghost' className='rounded-full px-4'>
                Projects
              </Button>
            </DropdownMenuTrigger>
            <AnimatePresence>
              {projectsOpen ? (
                <DropdownMenuContent align='start' className='w-64' forceMount asChild>
                  <motion.div
                    initial={{ opacity: 0, y: -12 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -12 }}
                    transition={{ duration: 0.2, ease: 'easeOut' }}
                  >
                    {renderProjectLinks()}
                  </motion.div>
                </DropdownMenuContent>
              ) : null}
            </AnimatePresence>
          </DropdownMenu>

          <div className='relative group'>
            <a
              href='mailto:masy370@gmail.com'
              className='text-sm font-medium text-muted-foreground transition hover:text-primary'
            >
              Contact
            </a>
            <span className='pointer-events-none absolute left-1/2 top-full mt-2 -translate-x-1/2 rounded-2xl border border-border/70 bg-card px-4 py-2 text-xs font-semibold opacity-0 shadow-sm transition-all duration-200 group-hover:pointer-events-auto group-hover:-translate-y-1 group-hover:opacity-100'>
              masy370@gmail.com
            </span>
          </div>
        </nav>

        <div className='flex items-center gap-2'>
          <ModeToggle />
          <Button
            variant='outline'
            size='icon'
            className='rounded-2xl md:hidden'
            onClick={() => setMobileOpen((prev) => !prev)}
            aria-label='Toggle menu'
          >
            {mobileOpen ? <X className='h-5 w-5' /> : <Menu className='h-5 w-5' />}
          </Button>
        </div>
      </div>

      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.25, ease: 'easeInOut' }}
            className='border-t border-border/60 bg-background/95 px-6 pb-4 pt-2 md:hidden'
          >
            <div className='flex flex-col gap-3'>
              <div className='rounded-3xl border border-border/70 bg-card p-3'>
                <p className='mb-2 text-xs font-semibold text-muted-foreground'>Projects</p>
                <div className='flex flex-col gap-1.5'>
                  {projects.map((project) => (
                    <Link
                      key={project.path}
                      to={project.path}
                      className='rounded-2xl px-3 py-2 text-sm font-medium hover:bg-accent'
                    >
                      {project.title}
                    </Link>
                  ))}
                </div>
              </div>
              <a
                href='mailto:masy370@gmail.com'
                className='rounded-3xl border border-border/70 px-4 py-3 text-sm font-semibold hover:bg-accent'
              >
                Contact
              </a>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
