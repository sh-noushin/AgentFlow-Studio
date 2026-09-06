import asyncio
import sys
from pathlib import Path

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main() -> None:
    server_path = Path(__file__).with_name("server.py").resolve()

    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [str(server_path)],
            }
        }
    )

    tools = await client.get_tools()

    print("Tools:")

    for tool in tools:
        print(tool.name)

    add_tool = next(
        tool for tool in tools
        if tool.name == "add"
    )

    result = await add_tool.ainvoke(
        {
            "a": 10,
            "b": 20
        }
    )

    print("\nResult:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())