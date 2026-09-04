from mcp.server import MCPServer

mcp = FastMCP("AgentFlow MCP Tools")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def get_order_status(order_id: int) -> str:
    """Get the status of an order."""

    orders = {
        101: "Processing",
        102: "Shipped",
        103: "Delivered"
    }

    return orders.get(
        order_id,
        "Order not found"
    )


if __name__ == "__main__":
    mcp.run()