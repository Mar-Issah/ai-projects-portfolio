import { CircuitBoard } from "lucide-react"

import { AIPlaceholderPanel } from "../components/AIPlaceholderPanel"
import { ProjectPageLayout } from "../components/ProjectPageLayout"

export default function ToolAgentPage() {
  return (
    <ProjectPageLayout
      subtitle="Tool-Using Agent"
      title="APIs, meet autonomy"
      description="Chain external tools, monitor executions, and let users approve actions before anything irreversible happens."
      stats={[
        { label: "TOOLS", value: "REST + GraphQL" },
        { label: "ACTIONS", value: "Streaming" },
        { label: "SAFETY", value: "Human-in-loop" },
      ]}
    >
      <div className="space-y-6">
        <AIPlaceholderPanel
          title="Tool router"
          description="Queue jobs, route to the best tool, and observe structured outputs."
          ctaLabel="Run workflow"
        />

        <div className="rounded-3xl border border-dashed border-border/70 p-6 text-sm text-muted-foreground">
          <p className="flex items-center gap-2 text-base font-medium text-foreground">
            <CircuitBoard className="h-4 w-4 text-primary" />
            Shipping notes
          </p>
          <ul className="mt-3 list-disc space-y-2 pl-5">
            <li>Expose execution traces + API logs in the Output tab.</li>
            <li>Highlight tool costs + latency to keep teams honest.</li>
            <li>Add approvals + fallback tools for resilience.</li>
          </ul>
        </div>
      </div>
    </ProjectPageLayout>
  )
}

