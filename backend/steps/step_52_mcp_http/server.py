import uvicorn

from mcp.server import MCPServer


mcp = MCPServer("AgentFlow MCP HTTP Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


app = mcp.streamable_http_app(
    stateless_http=True
)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8765
    )

    #& .\backend\.venv\Scripts\python.exe .\backend\steps\step_52_mcp_http\client.py