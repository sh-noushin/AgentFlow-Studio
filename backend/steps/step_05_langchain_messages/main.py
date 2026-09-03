from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI


def main() -> None:
    load_dotenv()

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    messages = [
        SystemMessage(
            content="You are a senior software engineer and AI instructor."
        ),
        HumanMessage(
            content="Explain the difference between an LLM and an AI agent."
        ),
    ]

    response = model.invoke(messages)

    print(response.content)

    print("\nResponse type:")
    print(type(response))


if __name__ == "__main__":
    main()