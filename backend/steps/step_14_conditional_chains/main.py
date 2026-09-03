from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch
from langchain_google_genai import ChatGoogleGenerativeAI


def main() -> None:
    load_dotenv()

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    csharp_prompt = ChatPromptTemplate.from_template(
        "You are a senior C# developer. Explain this question: {question}"
    )

    angular_prompt = ChatPromptTemplate.from_template(
        "You are a senior Angular developer. Explain this question: {question}"
    )

    general_prompt = ChatPromptTemplate.from_template(
        "You are a senior software developer. Answer this question: {question}"
    )

    csharp_chain = csharp_prompt | model
    angular_chain = angular_prompt | model
    general_chain = general_prompt | model

    conditional_chain = RunnableBranch(
        (
            lambda input_data: "c#" in input_data["question"].lower(),
            csharp_chain
        ),
        (
            lambda input_data: "angular" in input_data["question"].lower(),
            angular_chain
        ),
        general_chain
    )

    response = conditional_chain.invoke(
        {
            "question": "What is dependency injection in C#?"
        }
    )

    print(response.content)


if __name__ == "__main__":
    main()