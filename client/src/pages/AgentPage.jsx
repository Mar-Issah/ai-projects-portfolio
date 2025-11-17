import { Lightbulb } from "lucide-react"

import { AIPlaceholderPanel } from "../components/AIPlaceholderPanel"
import { ProjectPageLayout } from "../components/ProjectPageLayout"
import { Button } from "../components/ui/button"

export default function AgentPage() {
  return (
    <ProjectPageLayout
      subtitle="AI Agent"
      title="Tool-aware agent copilots"
      description="Prototype goal-driven agents that can plan, call APIs, and explain their reasoning in plain English."
      stats={[
        { label: "TOOLS", value: "10+" },
        { label: "LATENCY", value: "<2s" },
        { label: "TRACE DEPTH", value: "5 hops" },
      ]}
    >
      <div className="space-y-6">
        <AIPlaceholderPanel
          title="Conversation sandbox"
          description="Ask the agent to complete tasks, inspect intermediate thoughts, and view the tool stack."
          ctaLabel="Dispatch agent"
        />

        <div className="rounded-3xl border border-dashed border-border/70 p-6 text-sm text-muted-foreground">
          <p className="flex items-center gap-2 text-base font-medium text-foreground">
            <Lightbulb className="h-4 w-4 text-primary" />
            Suggested wiring
          </p>
          <ul className="mt-3 list-disc space-y-2 pl-5">
            <li>Integrate LangGraph or CrewAI for multi-step planning.</li>
            <li>Log tool outputs into Supabase for auditability.</li>
            <li>Use the Controls tab to toggle available tools per task.</li>
          </ul>
          <Button variant="ghost" className="mt-4 rounded-full px-4">
            Need help wiring this? Let’s chat.
          </Button>
        </div>
      </div>
    </ProjectPageLayout>
  )
}

