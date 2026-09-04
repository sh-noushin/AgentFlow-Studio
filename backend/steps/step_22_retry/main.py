from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


def main() -> None:
    load_dotenv()

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    reliable_model = model.with_retry()

    result = reliable_model.invoke(
        "Explain what an AI agent is in one simple sentence."
    )

    print(result.content)


if __name__ == "__main__":
    main()