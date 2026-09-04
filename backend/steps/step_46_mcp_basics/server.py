#should be installed :pip install "mcp[cli]"

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("AgentFlow MCP Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


if __name__ == "__main__":
    mcp.run()