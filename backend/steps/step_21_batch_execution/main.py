from langchain_core.runnables import RunnableLambda


def double_number(number: int) -> int:
    return number * 2


def main() -> None:
    runnable = RunnableLambda(double_number)

    results = runnable.batch([1, 2, 3, 4, 5])

    print(results)


if __name__ == "__main__":
    main()