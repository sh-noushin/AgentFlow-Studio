#should be installed :pip install "mcp[cli]"

from mcp.server import MCPServer


mcp = MCPServer("AgentFlow MCP Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b