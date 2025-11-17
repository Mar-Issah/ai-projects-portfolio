import { Palette } from "lucide-react"

import { AIPlaceholderPanel } from "../components/AIPlaceholderPanel"
import { ProjectPageLayout } from "../components/ProjectPageLayout"

export default function TextToImagePage() {
  return (
    <ProjectPageLayout
      subtitle="Text-to-Image"
      title="Prompt the pixels"
      description="Experiment with style presets, aspect ratios, and upscalers—all in a playful, art-director friendly UI."
      stats={[
        { label: "STYLES", value: "20" },
        { label: "UPSCALE", value: "4K" },
        { label: "QUEUE", value: "<30s" },
      ]}
    >
      <div className="space-y-6">
        <AIPlaceholderPanel
          title="Creative studio"
          description="Write prompts, tweak guidance scale, and preview pending generations."
          ctaLabel="Render scene"
        />

        <div className="rounded-3xl border border-border/70 bg-card/80 p-6 text-sm text-muted-foreground">
          <p className="flex items-center gap-2 text-base font-semibold text-foreground">
            <Palette className="h-4 w-4 text-primary" />
            Hot takes
          </p>
          <p className="mt-2">
            Add tabs for reference boards, negative prompts, and seeded reruns. Build a history timeline so creatives can branch explorations.
          </p>
        </div>
      </div>
    </ProjectPageLayout>
  )
}

