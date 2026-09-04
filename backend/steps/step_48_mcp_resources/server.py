from mcp.server import MCPServer


mcp = MCPServer("AgentFlow MCP Resources")


@mcp.resource("config://app")
def get_app_config() -> str:
    """Get the application configuration."""
    return "AppName=AgentFlow Studio; Environment=Development"