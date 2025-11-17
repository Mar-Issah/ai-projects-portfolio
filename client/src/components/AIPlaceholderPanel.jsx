import { Bot, PanelLeft } from "lucide-react"

import { Button } from "./ui/button"
import { Input } from "./ui/input"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "./ui/tabs"
import { Textarea } from "./ui/textarea"

export function AIPlaceholderPanel({ title, description, ctaLabel = "Send prompt" }) {
  return (
    <section className="rounded-3xl border border-border/70 bg-card/90 p-6 shadow-sm">
      <div className="mb-6 flex items-center gap-3">
        <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-primary/10 text-primary">
          <Bot className="h-5 w-5" />
        </div>
        <div>
          <h2 className="text-xl font-semibold">{title}</h2>
          <p className="text-sm text-muted-foreground">{description}</p>
        </div>
      </div>

      <Tabs defaultValue="chat" className="w-full">
        <TabsList className="bg-muted/60">
          <TabsTrigger value="chat">Chat</TabsTrigger>
          <TabsTrigger value="output">Output</TabsTrigger>
          <TabsTrigger value="controls">Controls</TabsTrigger>
        </TabsList>
        <TabsContent value="chat">
          <div className="flex flex-col gap-4">
            <Textarea placeholder="Ask the agent anything..." />
            <Button className="self-end rounded-2xl px-6">{ctaLabel}</Button>
          </div>
        </TabsContent>
        <TabsContent value="output">
          <div className="space-y-3 rounded-3xl border border-dashed border-border/70 p-4 text-sm text-muted-foreground">
            <p>This area can display streamed responses, traces, or citations.</p>
            <p>You can wire it to any model output later.</p>
          </div>
        </TabsContent>
        <TabsContent value="controls">
          <div className="space-y-4">
            <Input placeholder="Dataset / endpoint" />
            <div className="rounded-3xl border border-border/70 p-4 text-sm text-muted-foreground">
              <p className="flex items-center gap-2 font-medium">
                <PanelLeft className="h-4 w-4" /> Suggested Controls
              </p>
              <ul className="mt-2 list-disc space-y-1 pl-5">
                <li>Temperature slider</li>
                <li>Tool selection checklist</li>
                <li>System prompt editor</li>
              </ul>
            </div>
          </div>
        </TabsContent>
      </Tabs>
    </section>
  )
}

