import { Radar } from "lucide-react"

import { AIPlaceholderPanel } from "../components/AIPlaceholderPanel"
import { ProjectPageLayout } from "../components/ProjectPageLayout"

export default function EmbeddingsPage() {
  return (
    <ProjectPageLayout
      subtitle="Embedding Explorer"
      title="Map the semantic space"
      description="Compare distances across providers, visualize outliers, and inspect neighbors in a clean interface."
      stats={[
        { label: "MODELS", value: "6" },
        { label: "DIMENSIONS", value: "1536" },
        { label: "LATENCY", value: "120ms" },
      ]}
    >
      <div className="space-y-6">
        <AIPlaceholderPanel
          title="Vector inspector"
          description="Drop in sample text, compute embeddings, and compare cosine similarity."
          ctaLabel="Generate vectors"
        />

        <div className="rounded-3xl border border-dashed border-border/70 p-6 text-sm text-muted-foreground">
          <p className="flex items-center gap-2 text-base font-medium text-foreground">
            <Radar className="h-4 w-4 text-primary" />
            Future ideas
          </p>
          <ul className="mt-3 list-disc space-y-2 pl-5">
            <li>Interactive PCA / UMAP scatterplot.</li>
            <li>Dataset versioning + drift alerts.</li>
            <li>Shareable reports for product teams.</li>
          </ul>
        </div>
      </div>
    </ProjectPageLayout>
  )
}

