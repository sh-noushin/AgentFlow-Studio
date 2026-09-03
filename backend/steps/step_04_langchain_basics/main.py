
# should be installed :python -m pip show langchain-google-genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


def main() -> None:
    load_dotenv()

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    response = model.invoke(
        "What is MCP"
    )

    print(response.content)


if __name__ == "__main__":
    main()