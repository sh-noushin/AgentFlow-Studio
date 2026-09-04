from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


def main() -> None:
    load_dotenv()

    primary_model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    fallback_model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash"
    )

    model_with_fallback = primary_model.with_fallbacks(
        [fallback_model]
    )

    result = model_with_fallback.invoke(
        "Explain AI agents in one simple sentence."
    )

    print(result.content)


if __name__ == "__main__":
    main()