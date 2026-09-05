from mcp.server import MCPServer


mcp = MCPServer("AgentFlow MCP stdio Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


if __name__ == "__main__":
    mcp.run()