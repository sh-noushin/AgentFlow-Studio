from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


@tool
def calculate_total(price: float, quantity: int) -> float:
    """Calculate the total price based on item price and quantity."""
    return price * quantity


def main() -> None:
    load_dotenv()

    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )

    model_with_tools = model.bind_tools(
        [calculate_total]
    )

    messages = [
        HumanMessage(
            content=(
                "I want to buy 4 items. "
                "Each item costs 19.50 euros. "
                "What is the total price?"
            )
        )
    ]

    ai_message = model_with_tools.invoke(messages)

    print("Tool calls:")
    print(ai_message.tool_calls)

    messages.append(ai_message)

    for tool_call in ai_message.tool_calls:
        tool_result = calculate_total.invoke(
            tool_call["args"]
        )

        print("\nTool result:")
        print(tool_result)

        messages.append(
            ToolMessage(
                content=str(tool_result),
                tool_call_id=tool_call["id"]
            )
        )

    final_response = model_with_tools.invoke(messages)

    print("\nFinal response:")
    print(final_response.content)


if __name__ == "__main__":
    main()