from langchain_core.runnables import RunnablePassthrough


def main() -> None:
    passthrough = RunnablePassthrough()

    result = passthrough.invoke("hello")

    print(result)


if __name__ == "__main__":
    main()