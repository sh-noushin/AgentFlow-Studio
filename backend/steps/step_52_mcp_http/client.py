import asyncio

import httpx2

from mcp import Client
from mcp.client.streamable_http import streamable_http_client


async def main() -> None:
    async with httpx2.AsyncClient(
        trust_env=False
    ) as http_client:

        transport = streamable_http_client(
            "http://127.0.0.1:8765/mcp",
            http_client=http_client
        )

        async with Client(transport) as client:
            result = await client.call_tool(
                "add",
                {
                    "a": 10,
                    "b": 20
                }
            )

            print(result.structured_content)


if __name__ == "__main__":
    asyncio.run(main())

    # & .\backend\.venv\Scripts\python.exe .\backend\steps\step_52_mcp_http\server.py