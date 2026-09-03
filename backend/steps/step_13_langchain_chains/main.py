from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


def main() -> None:
    load_dotenv()

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a senior software engineering instructor."
            ),
            (
                "human",
                "Explain {topic} to a {level} developer."
            ),
        ]
    )

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    chain = prompt | model

    response = chain.invoke(
        {
            "topic": "AI agents",
            "level": "beginner",
        }
    )

    print(response.content)


if __name__ == "__main__":
    main()