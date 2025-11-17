export function ProjectPageLayout({ title, subtitle, description, stats = [], children }) {
  return (
    <main className="mx-auto flex max-w-5xl flex-col gap-10 px-6 py-12">
      <div className="space-y-4 rounded-3xl border border-border/70 bg-card/90 p-8 shadow-sm">
        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-primary">{subtitle}</p>
        <h1 className="text-4xl font-semibold">{title}</h1>
        <p className="text-lg text-muted-foreground">{description}</p>
        {stats.length > 0 && (
          <div className="grid gap-4 sm:grid-cols-3">
            {stats.map((stat) => (
              <div key={stat.label} className="rounded-3xl border border-border/60 p-4 text-center">
                <p className="text-2xl font-semibold">{stat.value}</p>
                <p className="text-xs uppercase tracking-[0.3em] text-muted-foreground">{stat.label}</p>
              </div>
            ))}
          </div>
        )}
      </div>
      {children}
    </main>
  )
}

