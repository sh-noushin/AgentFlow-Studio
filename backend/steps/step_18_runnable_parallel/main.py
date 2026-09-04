from langchain_core.runnables import RunnableLambda, RunnableParallel


def double_number(number: int) -> int:
    return number * 2


def square_number(number: int) -> int:
    return number * number


def main() -> None:
    parallel = RunnableParallel(
        double=RunnableLambda(double_number),
        square=RunnableLambda(square_number)
    )

    result = parallel.invoke(5)

    print(result)


if __name__ == "__main__":
    main()