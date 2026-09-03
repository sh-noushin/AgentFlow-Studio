from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


def main() -> None:
    load_dotenv()

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a senior software engineer and AI instructor."
            ),
            (
                "human",
                "Explain {topic} for a {level} developer."
            ),
        ]
    )

    messages = prompt.invoke(
        {
            "topic": "tool calling",
            "level": "beginner",
        }
    )

    response = model.invoke(messages)

    print(response.content)


if __name__ == "__main__":
    main()