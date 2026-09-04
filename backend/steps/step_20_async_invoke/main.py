import asyncio

from langchain_core.runnables import RunnableLambda


def double_number(number: int) -> int:
    return number * 2


async def main() -> None:
    runnable = RunnableLambda(double_number)

    result = await runnable.ainvoke(5)

    print(result)


if __name__ == "__main__":
    asyncio.run(main())