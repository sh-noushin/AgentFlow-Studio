from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


def main() -> None:
    load_dotenv()

    prompt = ChatPromptTemplate.from_template(
        "Explain {topic} in one simple sentence."
    )

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    chain = prompt | model

    result = chain.invoke({
        "topic": "dependency injection"
    })

    print(result.content)


if __name__ == "__main__":
    main()