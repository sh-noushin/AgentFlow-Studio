from mcp.server import MCPServer


mcp = MCPServer("AgentFlow MCP Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.resource("config://app")
def get_app_config() -> str:
    """Get application configuration."""
    return "AppName=AgentFlow Studio"


@mcp.prompt()
def explain_topic(topic: str) -> str:
    """Create an explanation prompt."""
    return f"Explain {topic} in a simple way."