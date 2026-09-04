import asyncio

from mcp import Client

from server import mcp


async def main() -> None:
    async with Client(mcp) as client:
        result = await client.call_tool(
            "add",
            {
                "a": 2,
                "b": 3
            }
        )

        print(result.structured_content)


if __name__ == "__main__":
    asyncio.run(main())