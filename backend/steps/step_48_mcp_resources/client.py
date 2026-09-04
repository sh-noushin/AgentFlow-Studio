import asyncio

from mcp import Client
from mcp.types import TextResourceContents

from server import mcp


async def main() -> None:
    async with Client(mcp) as client:
        result = await client.read_resource(
            "config://app"
        )

        for content in result.contents:
            if isinstance(content, TextResourceContents):
                print(content.text)


if __name__ == "__main__":
    asyncio.run(main())