import asyncio

from mcp import Client

from server import mcp


async def main() -> None:
    async with Client(mcp) as client:

        tools = await client.list_tools()

        print("Tools:")

        for tool in tools.tools:
            print(tool.name)

        resources = await client.list_resources()

        print("\nResources:")

        for resource in resources.resources:
            print(resource.uri)

        prompts = await client.list_prompts()

        print("\nPrompts:")

        for prompt in prompts.prompts:
            print(prompt.name)


if __name__ == "__main__":
    asyncio.run(main())