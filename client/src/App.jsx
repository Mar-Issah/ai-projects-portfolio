import { Route, Routes } from "react-router-dom"

import { Navbar } from "./components/Navbar"
import AgentPage from "./pages/AgentPage"
import EmbeddingsPage from "./pages/EmbeddingsPage"
import HomePage from "./pages/HomePage"
import RagPage from "./pages/RagPage"
import TextToImagePage from "./pages/TextToImagePage"
import ToolAgentPage from "./pages/ToolAgentPage"

function App() {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/agent" element={<AgentPage />} />
        <Route path="/rag" element={<RagPage />} />
        <Route path="/embeddings" element={<EmbeddingsPage />} />
        <Route path="/text-to-image" element={<TextToImagePage />} />
        <Route path="/tool-agent" element={<ToolAgentPage />} />
      </Routes>
    </div>
  )
}

export default App
