import asyncio

from mcp import Client
from mcp.types import TextContent

from server import mcp


async def main() -> None:
    async with Client(mcp) as client:
        result = await client.get_prompt(
            "explain_topic",
            {
                "topic": "AI agents"
            }
        )

        for message in result.messages:
            if isinstance(message.content, TextContent):
                print(message.content.text)


if __name__ == "__main__":
    asyncio.run(main())