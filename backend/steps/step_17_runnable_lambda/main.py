from langchain_core.runnables import RunnableLambda


def to_upper(text: str) -> str:
    return text.upper()


def main() -> None:
    runnable = RunnableLambda(to_upper)

    result = runnable.invoke("hello")

    print(result)


if __name__ == "__main__":
    main()