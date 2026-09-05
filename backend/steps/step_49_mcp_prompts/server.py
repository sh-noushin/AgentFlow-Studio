from mcp.server import MCPServer


mcp = MCPServer("AgentFlow MCP Prompts")


@mcp.prompt()
def explain_topic(topic: str) -> str:
    """Create a simple explanation prompt."""
    return f"Explain {topic} in a simple way for a beginner."