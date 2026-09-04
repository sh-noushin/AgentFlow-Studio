import asyncio

from mcp import Client

from server import mcp


async def main() -> None:
    async with Client(mcp) as client:
        add_result = await client.call_tool(
            "add",
            {
                "a": 2,
                "b": 3
            }
        )

        multiply_result = await client.call_tool(
            "multiply",
            {
                "a": 4,
                "b": 5
            }
        )

        order_result = await client.call_tool(
            "get_order_status",
            {
                "order_id": 102
            }
        )

        print("Add:")
        print(add_result.structured_content)

        print("\nMultiply:")
        print(multiply_result.structured_content)

        print("\nOrder status:")
        print(order_result.structured_content)


if __name__ == "__main__":
    asyncio.run(main())