#should be installed :python -m pip install pydantic

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field


class TaskAnalysis(BaseModel):
    task_name: str = Field(
        description="A short name describing the requested task."
    )

    priority: str = Field(
        description="The priority of the task: low, medium, or high."
    )

    requires_approval: bool = Field(
        description="Whether the task requires human approval."
    )


def main() -> None:
    load_dotenv()

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    structured_model = model.with_structured_output(TaskAnalysis)

    result = structured_model.invoke(
        "Cancel order number 105 and refund the customer."
    )

    print(result)

    print("\nTask name:")
    print(result.task_name)

    print("\nPriority:")
    print(result.priority)

    print("\nRequires approval:")
    print(result.requires_approval)


if __name__ == "__main__":
    main()