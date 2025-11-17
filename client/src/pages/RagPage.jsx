import { ListChecks } from "lucide-react"

import { AIPlaceholderPanel } from "../components/AIPlaceholderPanel"
import { ProjectPageLayout } from "../components/ProjectPageLayout"

export default function RagPage() {
  return (
    <ProjectPageLayout
      subtitle="RAG Chatbot"
      title="Retrieval that explains itself"
      description="Pipe PDFs, Notion docs, or API responses into a vector DB, then see exactly which chunks power each answer."
      stats={[
        { label: "DOCS", value: "50+" },
        { label: "HITS", value: "Top-5" },
        { label: "EMB MODELS", value: "Any" },
      ]}
    >
      <div className="space-y-6">
        <AIPlaceholderPanel
          title="Grounded Q&A"
          description="Swap embedding models, adjust chunk sizes, and view highlighted citations."
          ctaLabel="Generate answer"
        />

        <div className="rounded-3xl border border-border/70 bg-card/80 p-6 text-sm text-muted-foreground">
          <p className="flex items-center gap-2 text-base font-semibold text-foreground">
            <ListChecks className="h-4 w-4 text-primary" />
            Launch checklist
          </p>
          <ol className="mt-3 list-decimal space-y-2 pl-5">
            <li>Upload dataset + pick embeddings provider.</li>
            <li>Configure retriever + reranker weights.</li>
            <li>Wire the Output tab to show contexts & feedback form.</li>
          </ol>
        </div>
      </div>
    </ProjectPageLayout>
  )
}

